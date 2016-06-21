# Given a string, test if every character in that string is unique

def isUnique(s):
    charSet = [False] * 128
    for char in s:
        if charSet[ord(char)]:
            return False
        else:
            charSet[ord(char)] = True
    return True

def testFunction(s, ans):
    print "testing " + s
    print "the answer should be " + str(ans)
    print "the test result is " + str(isUnique(s))


testFunction("ABCD", True)
testFunction("ABCA", False)
testFunction("DDDD", False)
