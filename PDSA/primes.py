def factors(n):
    factorslist = []
    for i in range(1,n+1):
        if n % i == 0:
            factorslist.append(i)
    return(factorslist)

print(factors(12))

def primes(n):
    return(factors(n) == [1,n])
primelist=[]
for i in range(1,101):
    if(primes(i)):
        primelist.append(i)
print(primelist)

