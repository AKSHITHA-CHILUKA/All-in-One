def is_prime(n):
  if n < 2 :
    return False
  for i in range(2, int(n ** 0.5)+1):
    if n % i == 0:
      return False
    return True
def twin_primes(n,m):
  twin_primes = []
  for a in range(n,m-1):
    if is_prime(a) and is_prime(a+2):
      twin_primes.append((a,a+2))
  return twin_primes

n = int(input("Enter the first number (n): "))
m = int(input("Enter the second number (m): "))

# Call the function and print the result
twin_prime_pairs = twin_primes(n, m)
print(sorted(twin_prime_pairs))
