/* 
Your goal in this kata is to implement a difference function,
which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in
list b keeping their order.

arrayDiff([1,2],[1]) == [2]

If a value is present in b, all of its occurrences must be 
removed from the other:

arrayDiff([1,2,2,2,3],[2]) == [1,3]
*/

function arrayDiff(array, data) {
    
    // RECORRER DATA TO DELETE
    for (let i = 0; i < data.length; i++) {

        // WHILE ARRAY INCLUDE DATA
        while (array.includes(data[i])) {

            // FOR EACH ELEMENT IN THE ARRAY...
            for (let y = 0; y < array.length; y++) {

                // ...VALIDATE IF INDEX IS EQUAL TO DATA
                if (array[y] == data[i]) {

                    // ELIMINATE IN THE INDEX Y
                    array.splice(y, 1)
                }
            }

        }
    }

    return array
}

a = arrayDiff([1,3,5,5,7,8,4,5], [5]);
console.log(a);
b = arrayDiff([1,3,5,5,7,1,8,4,5,1], [1,3]);
console.log(b);