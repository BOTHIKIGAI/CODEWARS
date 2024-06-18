/* 
Take 2 strings s1 and s2 including only letters from a to z. 
Return a new sorted string, the longest possible, containing 
distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

*/

function longest(s1, s2) {
    
    // 0. Variables
    let words = '' // words have the concatenation between s1 and s2 and after this convert to array
    let saveLetter = '' // save word to delete

    // 1. Join word
    words = s1 + s2
    
    // 2. Divide word by word and organizate
    words = words.split(''); // ejm: word = 'aaeeddzd' -> split -> ['a', 'e', 'e', ...]
    
    // 3. Iterar word array
    for (let i = 0; i < words.length; i++) {

        // 4. save letter
        saveLetter = words[0]

        // 5. delete all lette
        while (words.includes(saveLetter)) {

            // 6. for each element in words
            for (let y = 0; y < words.length; y++) {

                // 7. validate if letter is equal to saveLetter
                
                if (words[y] == saveLetter) {

                    // 8. delete letter
                    words.splice(y, 1)
                }
            }
        }
        
        // 9. add letter
        words.push(saveLetter);
    }

    // 10. organize array
    words = words.sort()
    words = words.join('');
   
    return words

}