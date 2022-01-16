class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0 or (x != 0 and x % 10 == 0 ):# negative integer can not be a palindrome number 
            return False;                     # if an integer ends with 0, it can not be a palindrome number
        
        y = 0;
        while(x > y):
            y = y * 10 + x % 10;
            x = x / 10;
        
        return x == y or x == y / 10; # store a Reverse Integer of half of x 
