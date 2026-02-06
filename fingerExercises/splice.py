
s = '1.23,2.4,3.123'
l = s.split(',')
a = 0

for i in l:
    a += float(i)
print(a)