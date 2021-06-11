dict1 = {
    "madat": "help",
    "aaj": "today",
    "abhi": "now"
    }

print("options are:", dict1.keys())

a = input("enter hindi word:\n")

print("the meaning of the word is", dict1.get(a))