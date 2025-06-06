import random

def game():
    print("Welcome to the number guessing game!")
    score = random.randint(1,100)
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
            
    print(f"Your score is {score}")
    if(score > hiscore):
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
    return score    

game()    