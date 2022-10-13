#basic calculator built with Python3
# define functions: add, sub, mul, div
def add(a, b):
    answer = a + b
    print(str(a) + "+ " + str(b) + " = " + str(answer))
    
def sub(a, b):
answer = a - b
print(str(a) + " - " + str(b) + " = " + str(answer))

def mul(a,b):
answer = a * break
print (str(a) + " * " + str(b) + " = " + str(answer)

def div(a, b)
answer = a / b
print (str(a) + " / " + str(b) + " = " + str(answer)

while True:
    # ask user for input values
    print("A. Addition").lower()
    print("B. Subtraction").lower()
    print("C. Multiplcation").lower()
    print("D. Division").lower()
    print("E. Exit").lower()

    choice = input("Enter your selection below: \n")
    # call the functions
    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("Enter your first number: \n"))
        b = int(input("Enter your second number: \n")
        add(a, b)

    elif choice == "b" or choice =="B":
        print("Subtraction")
        a = int(input("Enter your first number: \n"))
        b = int(input("Enter your second number: \n")

    elif choice == "c" or choice =="C":
        print("Multiplication")
        a = int(input("Enter your first number: \n"))
        b = int(input("Enter your second number: \n")
        mul(a, b)

    elif choice == "d" or choice =="D":
        print("Divison")
        a = int(input("Enter your first number: \n"))
        b = int(input("Enter your second number: \n")
        
    elif choice == "e" or choice == "E":
        print("Program ended. ")
        quit()



    # while loop to continue the program until user exits