
def factors(n):
    factorslist = []
    for i in range(1,n+1):
        if n % i == 0:
            factorslist.append(i)
    return(factorslist)


def primes(n):
    return(factors(n) == [1,n])
def prime_diffs(n):
    lastprime = 2
    pd = {}
    for i in range(3,n+1):
        if primes(i):
            d = i - lastprime
            lastprime = i
            if d in pd.keys():
                pd[d] = pd[d] + 1
            else:
                pd[d] = 1
    return(pd)
print(prime_diffs(40))