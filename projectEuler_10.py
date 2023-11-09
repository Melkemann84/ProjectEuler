import time
import pyperclip

# https://projecteuler.net/problem=10
'''
The sum of the primes below 10 is 17.
Find the sum of all the primes below two million.
'''

'''
# using this version (not ready to be implemented as is, tho), code runs on BlackBear in aprox 40minutes
def isPrime(num): # Returns True if prime, False if not
    if num > 1:
        if num == 2:
            return True
        if num != 2:
            for i in range(3, int(num/2)+1, 2): # Iterate from 2 to n / 2
                if (num % i) == 0:
                    return False
                    break
        else:
            return True
    else:
        return False
'''

def givePrimes(up_to):                          # Function returs array of all primes up to given limit
    primes = [True for i in range(up_to+1)]     # Boolean array of True
    p = 2                                       # 1 is not a prime
    while (p * p <= up_to):                     # every in between p and p*p is covered by another prime already. 3 -> 9, because 4(2), 5(prime), 6(2,3), 7(p), 8(2)
        if primes[p]:                           # if p of Primes == true, 
            for i in range(p * p, up_to+1,p):   # update next multiples of p to False. We start at next square, because every in between p and p*p is covered by another prime already
                primes[i] = False
        p += 1
    
    list_of_primes = []
    for p in range(2, up_to+1):                 #populate list where boolean array still is True
        if primes[p]:
            list_of_primes.append(p)
    return list_of_primes



def showMe(answer, start_time):  # returns answer in clipboard and calculates time used
    print("----------------------------------")
    print(f"The answer: {answer} has been copied to your clipboard!")
    print(f"--- {time.time() - start_time} seconds ---")
    print("----------------------------------")
    pyperclip.copy(str(answer))
    spam = pyperclip.paste()


start_time = time.time()
temp = givePrimes(2000000)
answer = sum(temp)
print(temp)
showMe(answer, start_time)