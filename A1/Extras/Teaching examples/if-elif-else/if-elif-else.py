input_user = input("Enter a word : ")
input_name = input("Enter a name : ")

if input_user == "Hello":
    print(f"Hello {input_name}")
elif input_user == "":
    print(f"Goodbye {input_name}")
else:
    print(f"See you later, {input_name}")