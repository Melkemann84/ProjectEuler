import time
import pyperclip

# https://projecteuler.net/problem=7
'''
By listing the first six prime numbers: 2,3,5,7,11 and 13, 
we can see that the 6th prime is 13.

What is the 10001st prime???
'''
def isPrime(num): #returns True if prime, False if not
    if num > 1:
        for i in range(2, int(num/2)+1): # Iterate from 2 to n / 2
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

        

def main(num):
    n = 0
    factors = []
    while len(factors) < num:
        if isPrime(n):
            factors.append(n)
        n = n+1
    return max(factors)


def showMe(answer,start_time): #returns answer in clipboard and calculates time used
    print("----------------------------------")
    print("The answer: " + str(answer)+" has been copied to your clipboard!")
    print("--- %s seconds ---" % (time.time() - start_time))
    print("----------------------------------")
    pyperclip.copy(str(answer))
    spam = pyperclip.paste()
    
start_time = time.time()
answer = main(10001)
showMe(answer,start_time)