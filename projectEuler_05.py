import time

# https://projecteuler.net/problem=5
''' Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers 
from 1 to 20?
'''

def isDevisable(num,rrange):    # returns True if num is divisible with whole rrange
    for i in range(1,rrange+1): # alternative: [7,8,11,13,16,17,18,19] 
        if num % i:
            return False
    return True


def main():
    i = 120
    while not isDevisable(i,20):
        i += 20
    return i

start_time = time.time()
answer = main()

print("--- %s seconds ---" % (time.time() - start_time))
print("----------------------------------")
print("Answer: " + str(answer))
print("----------------------------------")
#'''