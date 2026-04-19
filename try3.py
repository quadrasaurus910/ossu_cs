# Wrap try loop in a function

def readVal(valType, requestMsg, errorMsg): 
    while True:
        val = input(requestMsg + ' ') 
        try:
            return(valType(val)) #convert str to valType before returning 
        except ValueError:
            print(val, errorMsg)

val = readVal(int, 'Enter an integer:', 'is not an integer')

print(val)