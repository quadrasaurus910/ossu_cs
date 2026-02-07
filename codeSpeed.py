import datetime

maxVal = int(input('Enter a postive integer: ')) 
i=0
startTime = datetime.datetime.now()
while i < maxVal:
    i=i+1 
endTime = datetime.datetime.now()
delta = endTime - startTime
print(f"It took {delta} to count to {maxVal}") #startTime.strftime('%S %f'))