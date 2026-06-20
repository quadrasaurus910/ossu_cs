# Figire 10.3 showcases binary search implimented with recursion.

def search(L, e):
    """Assumes L is a list, the elements of which are in
    ascending order.
    Returns True if e is in L and False otherwise"""
    def bSearch(L, e, low, high): 
        #Decrements high - low
        if high == low:
            return L[low] == e 
        mid = (low + high)//2 
        print(f"low: {low}, mid: {mid}, high: {high}")
        if L[mid] == e:
            return True 
        elif L[mid] > e:
            if low == mid: #nothing left to search 
                return False
            else:
                return bSearch(L, e, low, mid - 1)
        else:
            return bSearch(L, e, mid + 1, high) # mid adds one and becomes the new low.
    if len(L) == 0: 
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)
    
# Create list and populate it with integers 1-50.
li = []
for i in range(1,51):
    li.append(int(i))

print(search(li, 50))
