def ad(num1,num2) :
    return num1 + num2
def su(num1,num2) :
    return num1 - num2
def mu(num1,num2) :
    return num1 * num2
def di(num1,num2) :
    return num1 / num2

n1 = float(input("Enter the number 1: "))
n2 = float(input("Enter the number 2: "))
print("Choose the operation you want to perform: + , - , / , * ")
ip = input()
if ip == "+" :
    print(f"Addition of {n1} and {n2} is: ", ad(n1,n2))
elif ip == "-" :
    print(f"Subtraction of {n1} and {n2} is: ", su(n1,n2))
elif ip == "*" :
    print(f"Multiplication of {n1} and {n2} is: ", mu(n1,n2))
elif ip == "/" :
    print(f"Division of {n1} and {n2} is: ", di(n1,n2))
else :
    print("Invalid Input: ")
