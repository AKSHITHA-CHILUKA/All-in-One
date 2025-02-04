def primes(n):
    res,i = True,2
    while(res and (i<n)):
        if (n%i) == 0:
            res = False
        i = i+1
    return(res)

print(primes(90))