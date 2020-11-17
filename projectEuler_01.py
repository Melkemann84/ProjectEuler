result = 0

def multiple(num):
    if num%3==0 or num%5==0:
        return num
    return 0

    

for n in range(1,1000):
    result = result + multiple(n)

print(result)