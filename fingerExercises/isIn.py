
def isIn():
    text1 = input('Enter text: ')
    text2 = input('Enter text: ')
    if text2 in text1:
        return True
    elif text1 in text2:
        return True
    else:
        return False
    
print(isIn())