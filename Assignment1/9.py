my_numbers = [7, 2, 4, 11, 19, 24, 66, 1, 42, 22, 37, 5, 3, 92, 73]
inp=input("enter a string: even or odd")
string=inp.lower()

if string == "even":
    even=[num for num in my_numbers if num % 2 == 0]
    print("even numbers:",even)
elif string=="odd":
    odd=[num for num in my_numbers if num % 2 != 0]
    print("odd numbers:", odd)
else:
    print("unknown input!")

