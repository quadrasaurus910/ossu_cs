
s = int(input('Enter a secret number: '))
# use boolean as a flag
found = False

for i in range(1, 11, 1):
    if i == s:
        print('found')
        # if signaled change flag to True
        found = True
if found == False:
    print('not found')