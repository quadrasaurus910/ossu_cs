import sys


def main():
    arglen = len(sys.argv)
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
            print(consecutiveInts(ints[0], ints[1], ints[2]))
        if arglen == 3:
            print(consecutiveInts(ints[0], ints[1]))



def consecutiveInts(s, n, offset=1):
    print((s - offset*n)/n)
    initial = (s  - (offset * n)) / n
    return [i for i in range(n)]

if __name__ == "__main__":
    main()