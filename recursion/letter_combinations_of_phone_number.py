"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = "2"
Output: ["a","b","c"]

As mentioned previously, we need to lock-in letters when we generate new letters. The easiest way to save state like this is to use recursion. Our algorithm will be as follows:

If the input is empty, return an empty array.

Initialize a data structure (e.g. a hash map) that maps digits to their letters, for example, mapping "6" to "m", "n", and "o".

Use a backtracking function to generate all possible combinations.

The function should take 2 primary inputs: the current combination of letters we have, path, and the index we are currently checking.
As a base case, if our current combination of letters is the same length as the input digits, that means we have a complete combination. Therefore, add it to our answer, and backtrack.
Otherwise, get all the letters that correspond with the current digit we are looking at, digits[index].
Loop through these letters. For each letter, add the letter to our current path, and call backtrack again, but move on to the next digit by incrementing index by 1.
Make sure to remove the letter from path once finished with it.

"""


def letterCombinations(self, digits: str) -> List[str]:
    # If the input is empty, immediately return an empty answer array
    if len(digits) == 0:
        return []

    # Map all the digits to their corresponding letters
    letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    def backtrack(index, path):
        # If the path is the same length as digits, we have a complete combination
        if len(path) == len(digits):
            combinations.append("".join(path))
            return  # Backtrack

        # Get the letters that the current digit maps to, and loop through them
        possible_letters = letters[digits[index]]
        for letter in possible_letters:
            # Add the letter to our current path
            path.append(letter)
            # Move on to the next digit
            backtrack(index + 1, path)
            # Backtrack by removing the letter before moving onto the next
            path.pop()

    # Initiate backtracking with an empty path and starting index of 0
    combinations = []
    backtrack(0, [])
    return combinations