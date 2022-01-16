class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""

        for i, _ in enumerate(s):
            candidate = self.get_palindrome(s, start = i, end = i)

            if len(candidate) > len(longest):
                longest = candidate

        return longest

    @staticmethod
    def get_palindrome(s, start, end):
        while end + 1 < len(s) and s[end+1] == s[start]:
            end += 1

        while start > 0 and end + 1 < len(s) and s[start - 1] == s[end + 1]:
            start -= 1
            end += 1

        return s[start:end + 1]
