print('CALCULATOR')
print('Select the operation you want to perform in the calculator:')
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
print("5. TRUNCATED DIVISION")
print("6. MODULUS")
print("7. EXPONENTIATION")

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "! Can't divide by zero !"

def truncated_division(x, y):
    if y != 0:
        return x // y
    else:
        return "! Can't divide by zero !"

def modulus(x, y):
    if y != 0:
        return x % y
    else:
        return "! Can't divide by zero !"

def exponentiation(x, y):
    return x ** y

while True:
    select = input("Enter your choice: ")

    if select in ["1", "2", "3", "4", "5", "6", "7"]:
        x = float(input("Enter the first decimal number: "))
        y = float(input("Enter the second decimal number: "))

        if select == "1":
            print("ADDITION:", addition(x, y))
        elif select == "2":
            print("SUBTRACTION:", subtraction(x, y))
        elif select == "3":
            print("MULTIPLICATION:", multiplication(x, y))
        elif select == "4":
            print("DIVISION:", division(x, y))
        elif select == "5":
            print("TRUNCATED DIVISION:", truncated_division(x, y))
        elif select == "6":
            print("MODULUS:", modulus(x, y))
        elif select == "7":
            print("EXPONENTIATION:", exponentiation(x, y))

        choice = input("Do you want to perform another calculation? (yes/no): ")
        if choice.lower() != "yes":
            break
    else:
        print('Invalid input! Please select a number from 1 to 7.')