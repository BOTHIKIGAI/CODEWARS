/* 
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more 
than one digit, continue reducing in this way until a single-digit 
number is produced. The input will be a non-negative integer
*/

function digitalRoot(n) {
    
    // 0. Variables
    endResult = 0;
    initialValue = 0;

    // 1. Transform to string and split the each letter
    n = n.toString().split('')


    while (n.length != 1) {

        // Transform array to int
        n = n.map(function(num) {
            return parseInt(num)
        })

        // Sum values 
        endResult = n.reduce(
            (accumulator, currentValue) => accumulator + currentValue, 
            initialValue,
        )

        n = endResult.toString().split('')
        
    }


    return parseInt(n[0])
    
}

console.log(digitalRoot(133));