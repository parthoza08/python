def remove(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Harry is a good      "
n = remove(this, "Harry")
print(n)