class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(i, dots, path):
            if dots == 4 and i == len(s):
                res.append(".".join(path))
                return
            if dots == 4 or i == len(s):
                return
            
            for j in range(i, min(i+3, len(s))):
                part = s[i:j+1]
                if (part[0] == '0' and len(part) > 1) or int(part) > 255:
                    break
                backtrack(j+1, dots+1, path+[part])

        backtrack(0, 0, [])
        return res
