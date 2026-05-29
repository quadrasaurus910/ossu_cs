import sys


def main():
    if sys.argv != 4:
        ints = []
        for i in sys.argv[1:]:
            try:
                ints.append(int(i))
                print(i)
            except:
                sys.exit("Arguments must be integers")
        print(ints)
        print(consecutiveInts(ints[0], ints[1], ints[2]))


def consecutiveInts(s, n, offset=1):
    print((s - offset*n)/n)
    initial = (s  - (offset * n)) / n
    return [i for i in range(n)]

if __name__ == "__main__":
    main()