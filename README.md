# Jay Clark

Hello world, I’m @jayeclark, and I've been training to be a full stack software engineer since May 2021, focusing on the MERN stack at first with a plan to add MEAN, LAMP, and Ruby on Rails later in my training. At the moment I'm working on making sure I have a strong grasp of JavaScript fundamentals. I've been active on [Codewars](https://www.codewars.com/users/jayclark) since July 2021, and I participate on Leetcode occasionally as well.

## Contributing
I'm interested in contributing to projects on a volunteer basis. I'm specifically looking become more familiar with version control and with the project management tools that I might be expected to use in a developer role, especially JIRA. I have a talent for debugging, refactoring, and self-commenting code that I am eager to contribute to the right team.

## Versions

[Version 3.0 : Work in Progress](https://github.com/jayeclark/jayeclark/blob/main/README.md#version-30-work-in-progress)  
[Version 2.1 : Startup Life](https://github.com/jayeclark/jayeclark/blob/main/README.md#version-21-startup-life)  
[Version 2.0 : California Dreamin](https://github.com/jayeclark/jayeclark/blob/main/README.md#version-20-california-dreamin)  
[Version 1.1 : Doctor Doctor](https://github.com/jayeclark/jayeclark/blob/main/README.md#version-11-doctor-doctor)  
[Version 1.0 : Harvard, Here I Come](https://github.com/jayeclark/jayeclark/blob/main/README.md#version-10-harvard-here-i-come)  

### Version 3.0 : Work in Progress  
When the pandemic put my executive job on pause, I reflected on my past roles - none of which had been quite the right fit. I'd spent my early career choosing the easiest and most convenient option, instead of seeking out the right role and industry and putting in effort to work toward that goal. I started to give serious, deep thought to what that 'right' industry and role might be, and realized I'd felt most fulfilled (and most useful) applying technology to solve business problems. 

In May 2021, I took the humbling step of completely rebooting my career, starting over from scratch as a software engineer. For years, friends & family told me I was too old to be able to catch up, that it was too difficult, or that I wouldn't enjoy it. As I hope my portfolio (coming soon) will demonstrate, they were wrong.
  
### Version 2.1 : Startup Life  
My partner, a game industry executive, saw that Twitch streamers needed help running their businesses, especially on paid collaborations with publishers and brands. As COO, I grew that observation from an idea into a renowned talent management business that was covered in the New Yorker and CNN. I coded more than 160 custom functions for our CRM system that automated daily tasks, provided insights into business bottlenecks, auto-generated contracts, and used APIs to integrate with Google Calendar, QuickBooks Online, and Docusign. 

Though the venture did not survive the pandemic, I'm grateful for the experience - and especially grateful that when the business shuttered, our displaced employees all found new roles quickly. 
  
### Version 2.0 : California Dreamin  
I moved to San Diego and worked as an analyst for an award-winning consulting firm. While there, I designed and built a web app for real-time GPS tracking, reservation processing, and dispatch of a fleet of several dozen airport shuttles - an app that was somehow, against all odds, successfully kludged together from WordPress components and custom PHP snippets.
  
### Version 1.1 : Doctor Doctor  
I pursued a doctorate because I was interested in a career in academia, where I would constantly be learning new things and mentoring younger academics. During the PhD, I worked for Harvard's Program in Health Systems Improvement where I built a content management system for drafting, approving, and distributing monthly newsletters. My doctoral training taught me to teach and mentor others, to seek out new information and quickly build competence in new technical topics, and to work smarter, not harder - all skills that I bring to my coding today. 

Along the way, I realized that academia wasn't the path for me. Job scarcity meant I'd have little choice of where in the country my career would take me, and I wanted to live somewhere without winter.
  
### Version 1.0 : Harvard, Here I Come  
I landed a spot at one of the most highly selective and respected universities. To pay for my degree, I worked in marketing at a start-up ERP software developer while a full time student. My Hoopes Prize-nominated thesis on internet culture led me to be accepted to Harvard's History of Science PhD program. 

I took a gap year before my PhD to work in Corporate Strategy at a nonprofit biotech.
  
## Favorite Javascript Shortcuts
These are some of the favorite shortcuts I've come across for use in competitive programming and sites like Codewars & Leetcode.

**Ternary Operator**  
```javascript
// To save time & space in if/else blocks, use
let y = condition ? expressionIfTrue : expressionIfFalse

// instead of 
let y = '';

if (condition) { 
  y = expressionIfTrue;
} else { 
  y = expressionIfFalse;
}

// Keep in mind that this ternary operator format only works for single-line values or expressions. 
// If you want to do something more complicated, you'll have to write a helper function. 
// But the result is still likely to be easier to read and take up fewer lines of code. 
```

**String Spread Operator**  

```javascript 
// To create an array out of each letter in a string, use
let arr = [...str]

// instead of 
let arr = str.split('')
```
**+ Operator**  
```javascript
// To return the numeric representation of an object or variable, use
+[...'1234.56'].reverse().join('')

//instead of 
parseFloat([...'1234.56'].reverse().join(''))
```

**Convert Number to String**  
```javascript
// To convert a number to its base 10 string equivalent, use a template string like this:
let num = 12000
return `${num}`  // returns '12000' instead of 12000

//instead of
let num = 12000
return num.toString()

//or
let num = 12000
return '' + num
```

**Passing Arrays as Arguments**  
```javascript
/**
 * Sometimes you may find that you need to pass an array as an argument to function.
 * to avoid a lot of unnecessary [0], [1], etc. clutter, define the elements of the 
 * array when declaring the function: 
 */
let distance = ([x, y], [xC, yC]) => ((x - xC) ** 2 + (y - yC) ** 2) ** 0.5
let position = [1,1]
let center = [-1,2]

return distance(position,center)


//instead of
let distance = (position, center) => ((position[0] - center[0]) ** 2 + (position[1] - center[1]) ** 2) ** 0.5
let position = [1,1]
let center = [-1,2]

return distance(position,center)


//or
let distance = (x, y, xC,yC) => ((x - xC) ** 2 + (y - yC) ** 2) ** 0.5
let position = [1,1]
let center = [-1,2]

myFunc(position[0],position[1],center[0],center[1])

/**
 * Of course, you could also just store the initial data as four variables 
 * (x, y, xC, yC), but this shortcut is specifically relevant to situations where 
 * you might be iterating through an array of arrays and want to maximize code 
 * readability and simplicity
 */
```


<!---
jayeclark/jayeclark is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
