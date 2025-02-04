def prime(n):
    res = True
    for i in range(2,n):
        if n % i == 0 :
            res = False
            break
    return(res)

print(prime(102))