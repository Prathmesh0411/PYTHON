f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("twinkele found")
else:
    print("twinkle not found")
    
f.close()