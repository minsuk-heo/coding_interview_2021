"""
Input: num1 = "2", num2 = "3"
Output: "6"

Input: num1 = "123", num2 = "456"
Output: "56088"
"""


def multiply(num1: str, num2: str) -> str:
    int_num = 0
    for i in num1:
        int_num = int_num * 10
        int_num += (ord(i) - ord('0'))

    int_num2 = 0
    for i in num2:
        int_num2 = int_num2 * 10
        int_num2 += (ord(i) - ord('0'))
    return str(int_num * int_num2)

print(multiply("12", "11"))