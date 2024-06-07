try:
    file = open("masterpiece.txt")
except FileNotFoundError as e:
    print("file not found")
except:
    print("unknown error")
