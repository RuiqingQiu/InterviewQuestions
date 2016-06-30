# Given a string, write a function to check if it is a permutation of a palidrome.
# Input: Tact Coa
# Output: True (permutation: taco cat, atcocta

def checkPalindromePermutation(input_str):
    letter_count = {}
    lower_str = input_str.lower()
    for letter in lower_str:
        if letter <= 'z' and letter >= 'a':
            letter_count[letter] = 0
    for letter in lower_str:
        if letter <= 'z' and letter >= 'a':
            letter_count[letter] = letter_count[letter] + 1
    print letter_count
    hasOneOdd = False
    for key in letter_count:
        if letter_count[key] % 2 != 0:
            if hasOneOdd == False:
                hasOneOdd = True
            else:
                return False
    if hasOneOdd == False:
        return False
    else:
        return True




print checkPalindromePermutation("hello")
print checkPalindromePermutation("Tact Coa")
