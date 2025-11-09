from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        t_count = Counter(t)
        window = {}
        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float('inf')
        left = 0
        
        for right, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            
            if c in t_count and window[c] == t_count[c]:
                have += 1
            
            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1
        
        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""
