import time
start_time = time.time()

# https://projecteuler.net/problem=1
# Multiples of 3 and 5

def multiple(num):
    if num%3==0 or num%5==0:
        return num
    return 0

def Main():
    result = 0
    for n in range(1,1000):
        result = result + multiple(n)
    return result


answer = Main()


print("--- %s seconds ---" % (time.time() - start_time))
print("----------------------------------")
print("result: " + str(answer))
print("----------------------------------")
