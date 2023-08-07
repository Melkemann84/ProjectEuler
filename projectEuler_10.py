import time
import pyperclip

# https://projecteuler.net/problem=10
'''
The sum of the primes below 10 is 17.
Find the sum of all the primes below two million.
'''
def isPrime(num): # Returns True if prime, False if not
    if num > 1:
        for i in range(2, int(num/2)+1): # Iterate from 2 to n / 2
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

def main(upper_limit):
    list_of_primes = [0]
    for i in range(upper_limit):
        if i % 1000 == 0:
            print(f"We are currently at {i}")
        if isPrime(i):
            list_of_primes.append(i)
    result = sum(list_of_primes)
    return result


def showMe(answer, start_time):  # returns answer in clipboard and calculates time used
    print("----------------------------------")
    print(f"The answer: {answer} has been copied to your clipboard!")
    print(f"--- {time.time() - start_time} seconds ---")
    print("----------------------------------")
    pyperclip.copy(str(answer))
    spam = pyperclip.paste()


start_time = time.time()
answer = main(2000000)
showMe(answer, start_time)