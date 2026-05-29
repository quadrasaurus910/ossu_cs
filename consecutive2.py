import sys


def main():
    if sys.argv != 4:
        ints = []
        for i in sys.argv:
            try:
                ints.append(int(i))
            except:
                sys.exit("Arguments must be integers")
        consecutiveInts(ints[:])


def consecutiveInts(s, n, offset=1):
    ...

consecutiveInts(1,2)