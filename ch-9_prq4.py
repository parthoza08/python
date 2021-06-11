content=""
with open("file.txt") as f:
    content = f.read()
    print(content)

content = content.replace("donkey", "^$^&%^%#")
print(content)

with open("file.txt", "w") as r:
    r.write(content)