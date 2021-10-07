# Jay Clark

Hello world, I’m @jayeclark, and I've been training to be a full stack software engineer since May 2021, focusing on the MERN stack at first with a plan to add MEAN, LAMP, and Ruby on Rails later in my training. At the moment I'm working on making sure I have a strong grasp of JavaScript fundamentals. I've been active on [Codewars](https://www.codewars.com/users/jayclark) since July 2021, and I participate on Leetcode occasionally as well.

## Contributing
I'm interested in contributing to projects on a volunteer basis. I'm specifically looking become more familiar with version control and with the project management tools that I might be expected to use in a developer role, especially JIRA. I have a talent and tenacity for debugging, refactoring, and self-commenting code that I am eager to contribute to the open source community.

## Versions

[Version 3.0 : Work in Progress](https://github.com/jayeclark/jayeclark/blob/main/versions.md#version-30--work-in-progress)  
[Version 2.1 : Startup Life](https://github.com/jayeclark/jayeclark/blob/main/versions.md#version-21--startup-life)  
[Version 2.0 : California Dreamin](https://github.com/jayeclark/jayeclark/blob/main/versions.md#version-20--california-dreamin)  
[Version 1.1 : Doctor Doctor](https://github.com/jayeclark/jayeclark/blob/main/versions.md#version-11--doctor-doctor)  
[Version 1.0 : Harvard, Here I Come](https://github.com/jayeclark/jayeclark/blob/main/versions.md#version-10--harvard-here-i-come)  

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
