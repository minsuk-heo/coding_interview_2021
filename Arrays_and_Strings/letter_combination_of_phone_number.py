"""Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

"""


def letterCombinations(digits: str):
    d = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def print_comb(idx, prev_chars, cur_arr, total_cnt):
        nonlocal ans
        if idx == total_cnt:
            return
        val = d[digits[idx]]
        for ch in val:
            cur_arr.append(prev_chars + ch)
            if idx + 1 == total_cnt:
                ans.append(prev_chars + ch)
            print_comb(idx + 1, prev_chars + ch, cur_arr, total_cnt)

    ans = []
    print_comb(0, "", [], len(digits))
    return ans

print(letterCombinations("23"))