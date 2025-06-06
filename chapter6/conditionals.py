a = int(input("Enter the age of a:"))

if(a>18):
    print("Congratulations! you are eligible to vote")
    print("you are adult now")
    
elif(a<=0):
    print("please enter a valid age")
else:
    print("sorry you are not eligible to vote")