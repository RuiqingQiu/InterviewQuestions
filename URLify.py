# input "Mr John Smith", 13
# Output "Mr%20John%20Smith"

def URLify(str1, length):
    return str1.replace(" ", "%20")

print URLify("Mr John Smith", 13)
