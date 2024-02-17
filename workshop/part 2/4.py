utf8_value=int(input("enter a utf-8 value between 32 and 126"))
if 32<=utf8_value<=126:
    character= chr(utf8_value)
    print("the character is:", character)
else:
    print("the value must be between 32 and 126")