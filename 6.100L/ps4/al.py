m = 'test'
p = [50,50,50,50]

cm = ''

for i in range(len(m)):
    c = ord(m[i])
    cMod = c % 95

a = ord('a')
aMod = (a + 95) % 95
print(f"a: {a}, aMod: {aMod}")