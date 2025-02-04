def factors(n):
    factorslist = []
    for i in range(1,n+1):
        if n % i == 0:
            factorslist.append(i)
    return(factorslist)


def primes(n):
    return(factors(n) == [1,n])

def first_primes(m):
    (count,i,p1) = (0,1,[])
    while(count<m):
        if primes(i):
            (count,p1) = (count+1 , p1+[i])
        i = i+1
    return(p1)
print(first_primes(20))