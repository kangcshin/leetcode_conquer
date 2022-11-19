# Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

# The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

 

# Example 1:

# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# Example 2:

# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]
# Explanation:
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10

class Solution:

        
    def diffWaysToCompute(self, input, memo={}):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        if input in memo:
            return memo[input] 
        res = []
        for i in range(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, input[i]))
        memo[input] = res
        return res

    def helper(self, m, n, op):
        if op == "+":
            return m+n
        elif op == "-":
            return m-n
        else:
            return m*n
 
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit(): return [int(input)]
        res = []
        for i, c in enumerate(input):
            if c in '+-*':
                l = self.diffWaysToCompute(input[:i])
                r = self.diffWaysToCompute(input[i+1:])
                res.extend(a+b if c=='+' else a-b if c=='-' else a*b for a in l for b in r)
        return res