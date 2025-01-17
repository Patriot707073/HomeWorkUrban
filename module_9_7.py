def is_prime(func):
    def wrappper(*arf):
        res = func(*arf)
        prime = True
        for i in range (2, res - 1):
            if res % i == 0:
                prime = False
                break
        if prime:
            print('Простое')
        else:
            print('Составное')
        return res
    return wrappper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)
