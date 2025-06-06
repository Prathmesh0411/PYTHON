l = input("Enter name separated by space:").split()
for name in l:
    if(name.startswith("U")):
        print(f"Hello {name}")