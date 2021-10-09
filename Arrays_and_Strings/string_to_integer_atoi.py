"""
The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.

Input: s = "42"
Output: 42
Input: s = "   -42"
Output: -42
"""
def myAtoi(string: str) -> int:
    stripped = string.strip()
    sign = 1

    if not stripped:
        return 0

    elif stripped[0] in ("+", "-"):
        if stripped[0] == "-":
            sign = -1
        stripped = stripped[1:]
    elif not stripped[0].isdigit():
        return 0

    if not stripped:
        return 0
    try:
        ans = int(stripped[0])
        stripped = stripped[1:]

        for c in stripped:
            if c.isdigit():
                ans = ans * 10 + int(c)
            else:
                break

        if sign == 1:
            return sign * ans if ans < 2 ** 31 else 2147483647
        return -ans if ans <= 2 ** 31 else -2147483648
    except:
        return 0

s = "   -42"
assert (myAtoi(s) == -42)
