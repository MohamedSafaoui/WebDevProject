#  FizzBuzzBuggy.py

# Print every number from 1 to 100 (both included) on a new line.
# Numbers which are multiple of 3, print “Fizz” instead of a number.
# For the numbers which are multiples of 5, print “Buzz” instead of
# a number. For the number which is multiple of both 3 and 5, print
# “FizzBuzz” instead of numbers.

# OUTPUT from 1 to 15:
'''
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
'''


for num in range(1, 101):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
