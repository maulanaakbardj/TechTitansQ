# import library
import numpy as np

# Function to print the character and its 
# frequency in order of its occurrence
def prCharWithFreq(str) :
    
    # Size of the 'str'
    n = len(str)
    
    # Initialize all elements of freq[] to 0
    freq = np.zeros(26, dtype = np.int)

    # Accumulate frequency of each 
    # character in 'str'
    for i in range(0, n) :
        freq[ord(str[i]) - ord('a')] += 1 
                
    # Traverse 'str' from left to right
    for i in range(0, n) :
        
        # if frequency of character str[i]  
        # is not equal to 0
        if (freq[ord(str[i])- ord('a')] != 0) :
            
            # print the character along 
            # with its frequency
            print (str[i], freq[ord(str[i]) - ord('a')], 
                                                end = " ")

            # Update frequency of str[i] to 0 so that
            # the same character is not printed again
            freq[ord(str[i]) - ord('a')] = 0
        
    
# Driver Code
if __name__ == "__main__" :
    
    str = "geks";
    prCharWithFreq(str);
