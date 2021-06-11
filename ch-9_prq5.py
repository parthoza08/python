content=""
list1=["donkey", "kadu", "hell"]
with open("file.txt") as f:
    content = f.read()
    print(content)
 
for items in list1:
    content=content.replace(items, "$!&%!^")

with open("file.txt", "w") as h:
    h.write(content)