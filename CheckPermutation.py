# Given two strings, write a method to decide if one is a permutation of the other
# Idea: sort then compare

def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    new_str1 = ''.join(sorted(str1))
    new_str2 = ''.join(sorted(str2))
    if new_str1 == new_str2:
        return True
    else:
        return False

def testFunction(s1, s2, ans):
    print "testing " + s1 + ", " + s2
    print "the answer should be " + str(ans)
    print "the test result is " + str(checkPermutation(s1, s2))

testFunction("ABC", "CBA", True)
testFunction("ABC ", "CBA", False)
testFunction("AABBCC", "ABCABC", True)
testFunction("ABC", "abc", False)

# Idea 2: check if the two strings have identical character counts
def checkPermutation2(str1, str2):
    if len(str1) != len(str2):
        return False
    letters = [0] * 128
    for char in str1:
        letters[ord(char)] = letters[ord(char)] + 1
    for char in str2:
        letters[ord(char)] = letters[ord(char)] - 1
        if letters[ord(char)] < 0:
            return False
    return True

def testFunction2(s1, s2, ans):
    print "testing " + s1 + ", " + s2
    print "the answer should be " + str(ans)
    print "the test result is " + str(checkPermutation2(s1, s2))
testFunction2("ABC", "CBA", True)
testFunction2("ABC ", "CBA", False)
testFunction2("AABBCC", "ABCABC", True)
testFunction2("ABC", "abc", False)
