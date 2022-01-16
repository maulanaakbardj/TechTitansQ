// C# implementation to print the 
// character and its frequency in 
// order of its occurrence
using System;

class GFG {
    static int SIZE = 26;

    // function to print the character and its
    // frequency in order of its occurrence
    static void printCharWithFreq(String str)
    {
        // size of the string 'str'
        int n = str.Length;

        // 'freq[]' implemented as hash table
        int[] freq = new int[SIZE];

        // accumulate frequency of each character
        // in 'str'
        for (int i = 0; i < n; i++)
            freq[str[i] - 'a']++;

        // traverse 'str' from left to right
        for (int i = 0; i < n; i++) {

            // if frequency of character str.charAt(i)
            // is not equal to 0
            if (freq[str[i] - 'a'] != 0) {

                // print the character along with its
                // frequency
                Console.Write(str[i]);
                Console.Write(freq[str[i] - 'a'] + " ");

                // update frequency of str.charAt(i) to
                // 0 so that the same character is not
                // printed again
                freq[str[i] - 'a'] = 0;
            }
        }
    }

    // Driver program to test above
    public static void Main()
    {
        String str = "geks";
        printCharWithFreq(str);
    }
}
