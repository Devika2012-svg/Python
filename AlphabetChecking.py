character = input("Enter a character: ")

print(">>>>>>>Recognising the character<<<<<<<<")
if (character >= 'A' and character <= 'Z') or (character >= 'a' and character <= 'z'):
    print("It is an alphabet. 🅰")

elif character >= '0' and character <= '9':
    print("It is a number. 1️⃣")

elif character == '*' or character == '@' or character == '!' or character == '#' or character == '?' or character == '&' or character == '*'   :
    print("It is a special character. ❗")

else:
    print("Character not recognized.")
