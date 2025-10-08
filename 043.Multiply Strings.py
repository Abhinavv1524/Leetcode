class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        n, m = len(num1), len(num2)
        ans = [0] * (n + m)
        
        # Multiply each digit
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                sum_ = mul + ans[i + j + 1]
                
                ans[i + j + 1] = sum_ % 10
                ans[i + j] += sum_ // 10
        
        # Skip leading zeros
        result = []
        for num in ans:
            if not (len(result) == 0 and num == 0):
                result.append(str(num))
        
        return ''.join(result) if result else "0"