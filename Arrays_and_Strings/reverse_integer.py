"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

"""


def reverse(x: int) -> int:
    x_str = str(x)
    if len(x_str) < 2:
        return int(x_str)

    negative = False

    if x_str[0] == "-":
        negative = True
        x_str = x_str[1:]
    x_str_r = x_str[::-1]
    if negative:
        ans = -1 * int(x_str_r)
        if ans <= 2 ** 31 * -1:
            return 0
        else:
            return ans
    else:
        ans = int(x_str_r)
        if ans >= 2 ** 31 - 1:
            return 0
        else:
            return ans

print(reverse(12345))