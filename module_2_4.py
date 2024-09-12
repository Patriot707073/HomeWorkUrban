numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primers = []
not_primes = []
for i in numbers:
    if i<2:
        not_primes.append(i)
    else:
        is_prime = True
        for j in range (2,i):
            if i%j == 0:
                not_primes.append(i)
                is_prime = False
                break
        if is_prime:
            primers.append(i)

print (primers)
print (not_primes)






