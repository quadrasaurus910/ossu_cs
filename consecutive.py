def main():
    con(4, 136)

def con(a, n):
    """ Parameters: a is an int representing the amount of 
    consecutive integers. n is an int equal to sum of 
    consecutive integers starting at s.
    Returns list of consecutive integers"""
    offset = 0
    ci = []
    for i in range(1, a):
        offset += i * 2
    s = (n - offset) / a
    for i in range(a):
        ci.append(int(s) + i * 2)
    print(ci)


if __name__ == "__main__":
    main()