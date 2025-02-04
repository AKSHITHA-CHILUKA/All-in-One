import math
def primes(n):
    res,i = True,2
    while(res and (i<math.sqrt(n))):
        if (n%i) == 0:
            res = False
        i = i+1
    return(res)

print(primes(3))