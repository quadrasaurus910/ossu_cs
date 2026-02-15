num = int(input('Enter an integer: '))
if num < 0:
    is_neg = True
    num = abs(num)
else:
    is_neg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2
if is_neg:
    result = '-' + result
print(num, 'equals', result)