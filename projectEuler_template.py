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
    print(f"The answer: {answer} has been copied to your clipboard!")
    print(f"--- {time.time() - start_time} seconds ---")
    print("----------------------------------")
    pyperclip.copy(str(answer))
    spam = pyperclip.paste()
    
start_time = time.time()
answer = main()
showMe(answer,start_time)
