"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Input: s = ""
Output: 0

let dp[i] is the number of longest valid Parentheses ended with the i - 1 position of s, then we have the following relationship:
dp[i + 1] = dp[p] + i - p + 1 where p is the position of '(' which can matches current ')' in the stack.
"""

def longestValidParentheses(s):
    dp, stack = [0 for i in range(len(s)+1)], []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if stack:
                p = stack.pop()
                dp[i + 1] = dp[p] + i - p + 1
    return max(dp)

print(longestValidParentheses(")()()"))
