# ASCII printable characters range from 32 to 126

m = 'test '
p = [50,50,50,50,-50]

cm = ''
dc = ''

# lambda function to checkif char plus pad exceeds 126
lam = lambda chr,pad: ((ord(chr) + pad) > 126)

for i in range(len(m)):
    c = ord(m[i]) + p[i]
    if c > 126:
        c = (((ord(m[i]) + p[i]) - 32) % 95) + 32
    if c < 32:
        if c < 0:
            belowZ = abs(c)
        c = (((ord(m[i]) + p[i]) - 32) % 95) + 32
    cm += chr(c)
print(f"encrypted message: {cm}")

for i in range(len(cm)):
    c = (ord(cm[i]) - p[i])
    if c < 32:
        c = c + 95
    dc += chr(c)
print(dc)

a = ord('a')
aMod = (a + 95) % 95
aRem = a + 95 - 32
aRemMod = aRem % 95
# print(f"a: {a}, aMod: {aMod}, aRem: {aRem}, aRemMod: {aRemMod}")
if (lam(m[0],p[0])):
    rem = ord(m[0]) + p[0] - 32
    remMod = rem % 95
    # print(chr(remMod + 32))