def deep_copy(L):
    """L is a list that contains lists of lists etc."""
    print(L)
    if len(L) == 0:
        return []
    elif len(L) == 1:
        if type(L[0]) == list:
            return [deep_copy(L[0])]
        else:
            print(L[0])
            return [L[0]]
    else:
        if type(L[0]) == list:
            return [deep_copy(L[0])] + deep_copy(L[1:])
        else:
            return [L[0]] + deep_copy(L[1:])


myL = ['abc', ['d'], ['e', ['f', 'g']]]
myL2 = deep_copy(myL)
print(myL)
print(myL2)