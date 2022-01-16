class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret=0
        neg_flag = False
        if x<0:
            neg_flag = True
            x = x*(-1)
        while x!=0:
            ret=ret*10+x%10
            x=x/10
            if ret<=-2147483648 or ret >= 2147483647:
                return 0
        if neg_flag:
            ret = ret * -1
        return ret
