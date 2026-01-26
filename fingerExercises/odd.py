# determine if x, y, or z is odd, print largest odd number. 
# If none are odd print a message to that effect

x, y, z = 2,5, 9
l = [x, y, z]
sentence = "is the greatest odd number."

if x % 2 != 0:
    if y % 2 != 0:
        if z % 2 != 0:
            if x > y and x > z:
                print(f"x {sentence}")
            elif y > x and y > z:
                print(f"y {sentence}")
            else:
                print(f"z {sentence}")
        else:
            if x > y:
                print(f"x {sentence}")
            else:
                print(f"y {sentence}")
    else:
        print(f"y {sentence}")
elif y % 2 != 0:
    if z % 2 != 0:
        if y > z:
            print(f"y {sentence}")
        else:
            print(f"z {sentence}")
else:
    print(f"x {sentence}")

