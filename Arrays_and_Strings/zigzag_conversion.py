"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
"""
def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    bucket = []
    for i in range(numRows):
        bucket.append([])
    idx = 0
    asc = True
    for ch in s:
        bucket[idx].append(ch)
        if asc:
            if idx == numRows -1:
                asc = False
                idx -= 1
                continue
            else:
                idx += 1
        if not asc:
            if idx == 0:
                asc = True
                idx += 1
            else:
                idx -= 1
    res = ""
    for row in bucket:
        res += "".join(row)
    return res

s = "PAYPALISHIRING"
numRows = 3

print(convert(s, numRows))