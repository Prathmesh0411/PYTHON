p1 = "make a lots of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter the message:")

if (p1 in message) or (p2 in message) or (p3 in message) or (p4 in message):
    print("This message is spam")
    
else:
    print("This message is not spam")