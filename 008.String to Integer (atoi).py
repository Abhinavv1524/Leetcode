class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)
        result = 0
        sign = 1
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        while i < n and s[i] == " ":
            i += 1

        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1
            i += 1

        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            
            if sign == 1 and result > INT_MAX:
                return INT_MAX
            if sign == -1 and -result < INT_MIN:
                return INT_MIN

            i += 1

        return sign * result
