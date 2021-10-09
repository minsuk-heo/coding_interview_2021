"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true

"""
def isValid(s: str) -> bool:
    st = []
    d = {"[" :"]", "{" :"}", "(" :")"}
    open_brackets = set(['(', '[', '{'])
    for c in s:
        if c in open_brackets:
            st.append(c)
        else:
            if len(st) < 1:
                return False
            if d[st.pop()] != c:
                return False
    if len(st) > 0:
        return False
    return True

print(isValid("{[]}"))