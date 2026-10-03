"""Render github-stats.svg: past-year activity, public (full breakdown) vs private (total)."""
import datetime
import json
import os
import urllib.request

QUERY = """{ viewer { name login contributionsCollection { startedAt endedAt restrictedContributionsCount
  commitContributionsByRepository(maxRepositories: 100) { repository { isPrivate } contributions { totalCount } }
  pullRequestContributionsByRepository(maxRepositories: 100) { repository { isPrivate } contributions { totalCount } }
  pullRequestReviewContributionsByRepository(maxRepositories: 100) { repository { isPrivate } contributions { totalCount } }
  issueContributionsByRepository(maxRepositories: 100) { repository { isPrivate } contributions { totalCount } }
} } }"""


def fetch():
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY}).encode(),
        headers={"Authorization": f"bearer {os.environ['GH_TOKEN']}"},
    )
    with urllib.request.urlopen(req) as r:
        body = json.load(r)
    if "errors" in body:
        raise SystemExit(body["errors"])
    return body["data"]["viewer"]


def total(groups, private):
    return sum(g["contributions"]["totalCount"] for g in groups if g["repository"]["isPrivate"] == private)


def fmt(n):
    return f"{n:,}"


def render(viewer):
    c = viewer["contributionsCollection"]
    public = [
        ("Commits", total(c["commitContributionsByRepository"], False)),
        ("PRs opened", total(c["pullRequestContributionsByRepository"], False)),
        ("Reviews", total(c["pullRequestReviewContributionsByRepository"], False)),
        ("Issues", total(c["issueContributionsByRepository"], False)),
    ]
    # Private repos the token can't see are only reported as an undisclosed total.
    private_contributions = c["restrictedContributionsCount"] + sum(
        total(c[k], True)
        for k in (
            "commitContributionsByRepository",
            "pullRequestContributionsByRepository",
            "pullRequestReviewContributionsByRepository",
            "issueContributionsByRepository",
        )
    )

    start = datetime.date.fromisoformat(c["startedAt"][:10])
    today = datetime.date.today()
    period = f"{start:%b %Y} – {today:%b %Y}"

    cells = []
    for i, (label, n) in enumerate(public):
        x = 104 + i * 92
        cells.append(f'<text x="{x}" y="76" class="v">{fmt(n)}</text><text x="{x}" y="92" class="l">{label}</text>')
    cells.append(f'<text x="104" y="136" class="v">{fmt(private_contributions)}</text><text x="104" y="152" class="l">Contributions</text>')

    name = viewer["name"] or viewer["login"]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="480" height="176" viewBox="0 0 480 176">
<style>
  .bg {{ fill: #ffffff; stroke: #d0d7de; }}
  .t {{ fill: #1f2328; font: 600 15px -apple-system, "Segoe UI", Helvetica, Arial, sans-serif; }}
  .s, .l, .k {{ fill: #59636e; font: 12px -apple-system, "Segoe UI", Helvetica, Arial, sans-serif; }}
  .k {{ font-weight: 600; }}
  .v {{ fill: #1f2328; font: 600 20px -apple-system, "Segoe UI", Helvetica, Arial, sans-serif; }}
  .rule {{ stroke: #d8dee4; }}
  @media (prefers-color-scheme: dark) {{
    .bg {{ fill: #0d1117; stroke: #3d444d; }}
    .t, .v {{ fill: #f0f6fc; }}
    .s, .l, .k {{ fill: #9198a1; }}
    .rule {{ stroke: #3d444d; }}
  }}
</style>
<rect class="bg" x="0.5" y="0.5" width="479" height="175" rx="6"/>
<text x="20" y="30" class="t">{name}</text>
<text x="460" y="30" class="s" text-anchor="end">Past year · {period}</text>
<text x="20" y="76" class="k">Public</text>
<line class="rule" x1="20" x2="460" y1="110.5" y2="110.5"/>
<text x="20" y="136" class="k">Private</text>
{''.join(cells)}
</svg>
"""


if __name__ == "__main__":
    with open("github-stats.svg", "w") as f:
        f.write(render(fetch()))
