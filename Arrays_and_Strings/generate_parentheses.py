"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

"""


def generateParenthesis(n: int):
    ans = []

    def gen(prev, o, c, n):
        if c > o:
            return
        if o > n:
            return
        if o == n:
            if o - c == 0:
                ans.append(prev)
            else:
                gen(prev + ")", o, c + 1, n)

        if o < n:
            gen(prev + "(", o + 1, c, n)
            gen(prev + ")", o, c + 1, n)

    if n == 0:
        return []
    else:
        gen("(", 1, 0, n)
    return ans

print(generateParenthesis(3))