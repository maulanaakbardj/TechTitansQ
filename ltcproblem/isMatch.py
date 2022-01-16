class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == '':
            return s == ''
        if len(p) == 1:
            return len(s) == 1 and (s == p or p == '.')
        if p[1] != '*':
            if s == '':
                return False
            return (p[0] == s[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
        while s and (p[0] == s[0] or p[0] == '.'):
            if self.isMatch(s, p[2:]):
                return True
            s = s[1:]
        return self.isMatch(s, p[2:])
