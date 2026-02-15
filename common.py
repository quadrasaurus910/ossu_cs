
text1 = input('Enter text for text1: ')
text2 = input('Enter text for text2: ')
seen = ''

for c in text1 + text2:
    if c not in seen:
        seen += c

print(len(seen))