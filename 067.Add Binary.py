class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_val = int(a, 2) + int(b, 2)
        return bin(sum_val)[2:]
