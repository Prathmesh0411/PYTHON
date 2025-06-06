import random

computer = random.choice([-1,0,1])
youstr = input("Enter your choice:")
youDict = {"s": 1, "w": -1, "g": 0}   
reverseDect = {1: "snake", -1: "water", 0: "gun"}

you = youDict[youstr]
print(f"you chose {reverseDect[you]}\nComputer chose {reverseDect[computer]}")

if(computer == you):
    print("draw")
else:
    if(computer == -1 and you ==1):
        print("you win")
        
    elif(computer == -1 and you ==0):
        print("you lose")

    elif(computer == 1 and you == -1):
        print("you lose")    

    elif(computer == 1 and you == 0):
        print("you win")

    elif(computer == 0 and you == -1):
        print("you lose")
        
    elif(computer == 0 and you == 1):
        print("you win")
    else:
        print("something went wrong")
        