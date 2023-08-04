import time
import pyperclip

# https://projecteuler.net/problem=9
'''
A Pythagorean triplet is a set of three natural numbers, a<b<c, for wich, a*a + b*b = c*c.
For example, 3*3+4*4=5*5.
There exists exactly one Pythagorean triplet for which a+b+c=1000. Find the product.
'''

# Function to check if A,B and C are Pythagorean numbers. A<C | B<C
def isPythagorean(a,b,c):
    if (a*a + b*b) == c*c:
        return True
    else:
        return False
    
# Function to check if list contains unique numbers.
def isUnique(list):
    list.sort()
    list_is_unique = True
    for i in range(len(list)-1):
        if list[i] >= list[i+1]:
            list_is_uniqie = False
        if list_is_unique == False:
            return False
    return True
    

def main(sum_of_triplets):
    a = b = c = 0
    for c in range(sum_of_triplets/3+1):
        c = c+1
        for b in range(sum_of_triplets/3+1
    result = 0
    return result

def showMe(answer,start_time): #returns answer in clipboard and calculates time used
    print("----------------------------------")
    print(f"The answer: {answer} has been copied to your clipboard!")
    print(f"--- {time.time() - start_time} seconds ---")
    print("----------------------------------")
    pyperclip.copy(str(answer))
    spam = pyperclip.paste()
    
start_time = time.time()
answer = main()
showMe(answer,start_time)
