string1 = input("Enter a string: ")
string2 = input("Enter another string: ")
len_string1= len(string1)
len_string2= len(string2)

if len_string1>len_string2:
    print("String with max length:",string1)
elif len_string2>len_string1:
    print("String with max length:", string2)
else:
    print("both have same length")
    print(string1)
    print(string2)