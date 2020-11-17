
def primeFactors(num):
'''
*FIND PRIME FACTORS IN num*
Finds the smallest number that goes into num. Divides by this number.
Finds next small number that goes into new num.
When no new numbers goes into new num, it appends the last one.
'''
    i = 2 
    factors = []
    while i * i <= num:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(num)
    return factors

#print(primeFactors(13195))

n 30    15      5
i 2     3       5   

factors 2   3