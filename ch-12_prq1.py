def Printfile(filename):

    try:
        with open (filename, "r") as f:
            print(f.read())
        
    except FileNotFoundError:
        print("the File is missing")
    except :
        print("error occurred")

    

Printfile("1.txt")

