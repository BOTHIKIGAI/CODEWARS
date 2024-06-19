/* 
You probably know the "like" system from Facebook and other pages. 
People can "like" blog posts, pictures or other items. We want to
create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of 
people that like an item. It must return the display text as shown 
in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.

*/

function likes(names) {

    // 0. Variables
    numberLikes = names.length // Knowing the number of elements in the array
    message = ''; // message to return

    // 1. Validation number of likes
    if (numberLikes >= 1) {

        // 2. Add message persons
        message += numberLikes == 1 ? names[0] : numberLikes == 2 ? names[0] + ' and ' + names[1] : numberLikes == 3 ? names[0] + ', ' + names[1] + ' and ' + names[2] : names[0] + ', ' + names[1] + ' and ' + (numberLikes - 2) + ' others'

        // 3. Add message like
        message += `${numberLikes > 1 ? ' like' : ' likes'} this`


        return message
    }

    return 'no one likes this' // if the numbes likes is less than one
}

console.log(likes(["Max", "John", "Mark"]));