letter = '''Dear <|name|>,
            You are selected!
            <|Date|>'''
            
print(letter.replace("<|name|>", "Prathmesh").replace("<|Date|>", "1st Jan"))