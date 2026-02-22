# Lecture 5 finger exercise
# take input str and print even number indexed chars

my_str = input('Enter a str: ')
evens = ''

# Loop through each char in str
for i in range(len(my_str)):
    # check if even, if so append to output str
    if i % 2 == 0:
        evens += my_str[i]
print(evens)