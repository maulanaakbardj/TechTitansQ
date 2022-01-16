<?php 
// PHP implementation to print the 
// character and its frequency in
// order of its occurrence
$SIZE = 26;

// function to print the character and 
// its frequency in order of its occurrence
function printCharWithFreq($str)
{
    global $SIZE;
    
    // size of the string 'str'
    $n = strlen($str);

    // 'freq[]' implemented as hash table
    $freq = array_fill(0, $SIZE, NULL);

    // accumulate frequency of each 
    // character in 'str'
    for ($i = 0; $i < $n; $i++)
        $freq[ord($str[$i]) - ord('a')]++;

    // traverse 'str' from left to right
    for ($i = 0; $i < $n; $i++) 
    {

        // if frequency of character str[i] 
        // is not equal to 0
        if ($freq[ord($str[$i]) - ord('a')] != 0) 
        {

            // print the character along with 
            // its frequency
            echo $str[$i] . $freq[ord($str[$i]) - 
                                  ord('a')] . " ";

            // update frequency of str[i] to 0 
            // so that the same character is 
            // not printed again
            $freq[ord($str[$i]) - ord('a')] = 0;
        }
    }
}

// Driver Code
$str = "geks";
printCharWithFreq($str);

?>
