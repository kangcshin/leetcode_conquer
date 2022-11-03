# Given a balanced parentheses string s, return the score of the string.

# The score of a balanced parentheses string is based on the following rule:

# "()" has score 1.
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
 

# Example 1:

# Input: s = "()"
# Output: 1
# Example 2:

# Input: s = "(())"
# Output: 2
# Example 3:

# Input: s = "()()"
# Output: 2

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        out, count = 0, 0
        for i, x in enumerate(s):
            if x == '(':
                count += 1
            else:
                count -= 1
                if s[i-1] == '(':
                    # << is bits shifted by "counts" place
                    # this is the same as multiplying 1 by 2**count.
                    out += 1 << count
        return out
        