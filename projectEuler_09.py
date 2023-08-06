import time
import pyperclip

# https://projecteuler.net/problem=9
'''
A Pythagorean triplet is a set of three natural numbers, a<b<c, for wich, a*a + b*b = c*c.
For example, 3*3+4*4=5*5.
There exists exactly one Pythagorean triplet for which a+b+c=1000. Find the product.
'''

# Function to check if A,B and C are Pythagorean numbers. A<C | B<C
def isPythagorean(list):
    if (list[0]*list[0] + list[1]*list[1]) == list[2]*list[2]:
        return True
    else:
        return False

def main(target_sum_of_triplets):
    triplets = [0,0,0]
    for a in range(1,333): # A cannot be greater than 332<333<334<=1000
        triplets[0] = a
        for b in range(1,target_sum_of_triplets):
            triplets[1] = b
            for c in range(335,998): # C cannot be smaller than 335.
                triplets[2] = c
                if sum(triplets) == target_sum_of_triplets:
                    if isPythagorean(triplets):
                        print(triplets)
                        return triplets[0]*triplets[1]*triplets[2]
    return 0

def showMe(answer,start_time): #returns answer in clipboard and calculates time used
    print("----------------------------------")
    print(f"The answer: {answer} has been copied to your clipboard!")
    print(f"--- {time.time() - start_time} seconds ---")
    print("----------------------------------")
    pyperclip.copy(str(answer))
    spam = pyperclip.paste()
    
start_time = time.time()
answer = main(1000)
showMe(answer,start_time)
