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
