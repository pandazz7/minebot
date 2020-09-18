description = ("This script can remove conten frome file")
print(description)
while True:
    filename = input(("Enter file name in this direction:"))
    if filename == ("Exit"):
        exit("finishing...")
    else:
        file = open(filename, "w")
        print("File successfully opened")
        print("Are you sure you want to delete the contents of the file?(Yes/No/Exit)")
        while True:
            user_input = input("(Yes/No):")
            if user_input == ("Yes"):
                file.write("")
                print("Content of File successfully removed")
                file.close()
                print("File was closed")
                break
            elif user_input == ("No"):
                break
            elif user_input == ("Exit"):
                exit("finishing...")
            else:
                print("Unknown command, use'Yes' or 'No' or 'Exit'")
                continue
            continue