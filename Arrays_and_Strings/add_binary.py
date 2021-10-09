"""
Input: a = "11", b = "1"
Output: "100"

Input: a = "1010", b = "1011"
Output: "10101"

Convert a and b into integers x and y, x will be used to keep an answer, and y for the carry.

While carry is nonzero: y != 0:

Current answer without carry is XOR of x and y: answer = x^y.

Current carry is left-shifted AND of x and y: carry = (x & y) << 1.

Job is done, prepare the next loop: x = answer, y = carry.

Return x in the binary form.

"""


def addBinary(a: str, b: str) -> str:
    x, y = int(a, 2), int(b, 2)
    while y:
        answer = x ^ y
        carry = (x & y) << 1
        x, y = answer, carry
    return bin(x)[2:]
a = "1010"
b = "1011"
print(addBinary(a, b))