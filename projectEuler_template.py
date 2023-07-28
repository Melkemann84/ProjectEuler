import time
import pyperclip

# https://projecteuler.net/problem=
'''
'''

def main():
    result = 0
    return result

def showMe(answer,start_time): #returns answer in clipboard and calculates time used
    print("----------------------------------")
    print("The answer: " + str(answer)+" has been copied to your clipboard!")
    print("--- %s seconds ---" % (time.time() - start_time))
    print("----------------------------------")
    pyperclip.copy(str(answer))
    spam = pyperclip.paste()
    
start_time = time.time()
answer = main()
showMe(answer,start_time)