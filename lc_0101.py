class Solution:
    def maxScore(self, s: str) -> int:
        ttl_one = s.count('1')
        lft0 = 0
        rgt0 = 0
        masxcore = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                lft0 += 1
            else:
                rgt0 += 1
            score = lft0 + (ttl_one - rgt0)
            masxcore = max(masxcore, score)
        
        return masxcore
