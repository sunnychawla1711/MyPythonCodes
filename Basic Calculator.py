n1 = float(input("Enter the number 1: "))
n2 = float(input("Enter the number 2: "))
print("Choose the operation you want to perform: + , - , / , * ")
ip = input()
if ip == "+" :
    print(f"Addition of {n1} and {n2} is: ", n1+n2)
elif ip == "-" :
    print(f"Subtraction of {n1} and {n2} is: ", n1-n2)
elif ip == "*" :
    print(f"Multiplication of {n1} and {n2} is: ", n1*n2)
elif ip == "/" :
    print(f"Division of {n1} and {n2} is: ", n1/n2)
else :
    print("Invalid Input: ")
