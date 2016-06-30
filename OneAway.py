# Three types of edits: insert a character, remove a character, or replace
# a character. Given two strings, write a function to check if they are one
# edit (or zero edit) way
def OneAway(str1, str2):
    if(len(str1) == len(str2)):
        return oneEditReplace(str1, str2)
    elif(len(str1) + 1 == len(str2)):
        return oneEditInsert(str1, str2)
    elif(len(str1) - 1 == len(str2)):
        return oneEditInsert(str2, str1)
    else:
        return False
def oneEditReplace(str1, str2):
    foundDifference = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if foundDifference == False:
                foundDifference = True
            else:
                return False
    if foundDifference == True:
        return True
    else:
        return False

# The longer string is str1
def oneEditInsert(str1, str2):
    index1 = 0
    index2 = 0
    while(index2 < len(str2) and index1 < len(str1)):
        if(str1[index1] == str2[index2]):
            index1 = index1 + 1
            index2 = index2 + 1
        else:
            # This means there has already been one index that didnt match
            if index1 != index2:
                return False
            index2 = index2 + 1
    return True

print OneAway("pale", "ple")
print OneAway("pales", "pale")
print OneAway("pale", "bale")
print OneAway("pale", "bae")
