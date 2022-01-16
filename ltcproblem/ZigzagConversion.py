class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        if len(s) <= numRows:
            return s
        line = []
        skip = 2 * numRows - 2
        intervals = len(s) / skip
        for i in range(numRows):
            mods = [i]
            if i != 0 and i != numRows - 1:
                if skip - i < len(s):
                    mods.append(skip - i)
            idx = [j * skip + mod for j in range(intervals) for mod in mods]
            for mod in mods:
                if skip * intervals + mod < len(s):
                    idx.append(skip * intervals + mod)
            line += [s[j] for j in idx]
        return ''.join(line)
