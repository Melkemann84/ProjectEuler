import time

# https://projecteuler.net/problem=3
''' Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def primeFactors(num):
    i = 2 
    factors = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors

def main():

    return max(primeFactors(600851475143))

start_time = time.time()
answer = main()

print("--- %s seconds ---" % (time.time() - start_time))
print("----------------------------------")
print("Answer: " + str(answer))
print("----------------------------------")