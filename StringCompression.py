# 1.6 String Compression: Implement a method to perform basic string
# compression using the counts of repeated characters. For example,
# the string aabcccccaaa would become a2b1c5a3. If the "compressed" string
# not become smaller than the original string, your method should return the
# original string. You can assume the string has only uppercase and lowercase
# (a-z).
#Input: aabccccccaaa
#Output: a2b1c5a3
#Input: abcd
#Output: abcd

def StringCompression(string):
    old_len = len(string)
    new_str = ""
    cur_char = string[0]
    char_count = 0
    index = 0
    for char in string:
        if cur_char == char:
            char_count = char_count + 1
            if index == len(string)-1:
                new_str = new_str + cur_char + str(char_count)
        else:
            new_str = new_str + cur_char + str(char_count)
            char_count = 1
            cur_char = string[index]
        index = index + 1
    if len(new_str) > old_len:
        return string
    else:
        return new_str

print StringCompression("aabcccccaaa")
print StringCompression("abcd")

