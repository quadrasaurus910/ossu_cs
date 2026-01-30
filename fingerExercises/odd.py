# determine if x, y, or z is odd, print largest odd number. 
# If none are odd print a message to that effect

x, y, z = 7,9,11
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
            elif y > x:
                print(f"y {sentence}")
    else:
        if z % 2 != 0:
            if x > z:
                print(f"x {sentence}")
            elif z > x:
                print(f"z {sentence}")
        else:
            print(f"x {sentence}")
else:
    if y % 2 != 0:
        if z % 2 != 0:
            if y > z:
                print(f"y {sentence}")
            elif z > y:
                print(f"z {sentence}")
        else:
            print(f" y {sentence}")
    else:
        print("None of these numbers are odd")

