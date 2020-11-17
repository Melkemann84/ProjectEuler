import time

# https://projecteuler.net/problem=4
''' Larges palindrome product 
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
def isPalindrome(num):
    if str(num) == str(num)[::-1]:
       return True
    else:
        return False


def main():
    palindromes = []
    for m in range(1,999):
        for n in range (1,999):
            if isPalindrome(m*n):
                palindromes.append(m*n)

    return max(palindromes)


start_time = time.time()
answer = main()

print("--- %s seconds ---" % (time.time() - start_time))
print("----------------------------------")
print("Answer: " + str(answer))
print("----------------------------------")