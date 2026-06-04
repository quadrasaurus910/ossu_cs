import sys


def main():
    arglen = len(sys.argv)
    print(sys.argv)
    if arglen > 1:
        ints = []
        for i in sys.argv[1:]:
            try:
                ints.append(int(i))
                print(i)
            except:
                sys.exit("Arguments must be integers")
            ints.append(int(i))
        if arglen == 4:
            print(consecutiveInts(ints[1], ints[2], ints[3]))
        elif arglen == 3:
            print(consecutiveInts(ints[1], ints[2]))
        elif arglen == 2:
            na = input("Please enter amount of consecutive integers: ")
            print(consecutiveInts(ints[1], int(na)))
        elif arglen == 1:
            s = input("Please enter a sum: ")
            na = input("Please enter amount of consecutive integers: ")
            print(consecutiveInts(s, na))





def consecutiveInts(s, n, offset=1):
    print(f"s: {s}, n: {n}, offset: {offset}")
    print((s - offset*n)/n)
    initial = (s  - (offset * n)) / n
    return [i + initial for i in range(n)]

if __name__ == "__main__":
    main()