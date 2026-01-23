import random
SN = random.randint(1,10)
att = 0
print("Generating number between 1 to 10: ")
 
while att < 3:
    att = att+1
    n = int(input("Enter a number: "))
    if n == SN :
        print("You Guess it right: ")
        break
    elif n > SN :
        print("Guess a lower number: ")
    else : 
        print("Guess a larger number: ")
            
if att == 3 :
    print("You have loss the game: ")
