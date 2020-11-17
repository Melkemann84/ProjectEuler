import time
start_time = time.time()

#https://projecteuler.net/problem=2
#Even Fivonacci numbers

def fibonacciToo (lim):
    if lim == 0:
        return 0
    if lim == 1:
        return 1
    fib = [0,1]
    while fib[-2]+fib[-1] <= lim:
        fib.append (fib[-2]+fib[-1])
    return fib

def main():
    result = 0 
    for i in fibonacciToo(4000000):
        if i%2==0:
            result = result + i
    return result

answer = main()    

print("--- %s seconds ---" % (time.time() - start_time))
print("----------------------------------")
print("Answer: " + str(answer))
print("----------------------------------")