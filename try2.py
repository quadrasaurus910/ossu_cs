# Use while loop to ask for input till correct

while True:
    val = input('Enter an integer: ') 
    try:
        val = int(val)
        print('The square of the number you entered is', val**2) 
        break #to exit the while loop
    except ValueError:
        print(val, 'is not an integer')