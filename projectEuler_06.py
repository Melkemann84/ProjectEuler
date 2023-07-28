import time
import pyperclip


# https://projecteuler.net/problem=6
'''
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sumOfSquares(n): #returns the sum of the squares of the range 0 to n
    result = 0
    for i in range (1,n+1):
        result = result + i*i
    return result

def squareOfSum(n): #returns the square of the sum of the range 0 to n.
    result = 0
    for i in range (1,n+1): #sums the range
        result = result + i   
    result = result*result
    return result

def main():
    result = squareOfSum(100) - sumOfSquares(100) 
    return result

def present(answer):
    print("----------------------------------")
    print("The answer: " + str(answer)+" has been copied to your clipboard!")
    print("Time used: %s seconds ---" % (time.time() - start_time))
    print("----------------------------------")
    pyperclip.copy(str(answer))
    spam = pyperclip.paste()
    
start_time = time.time()
answer = main()
present(answer)