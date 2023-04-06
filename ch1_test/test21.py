primes = []
for num in range(3, 101):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
      primes.append(num)
    
print(primes)
print(len(primes))