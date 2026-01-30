def pick_primes(numbers):
    

    primes = []

    for num in numbers:
        if num < 2:
            continue

        is_prime = True
        
        # check divisors from 2 up to num-1
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes


print(pick_primes([12,3,7,18,11])) 
# [3, 7, 11]

print(pick_primes([17,23,9,42]))
# [17, 23]

print(pick_primes([4,2048,100,55]))
# []

        
        

print(pick_primes([12,3,7,18,11]))
# [3, 7, 11]

print(pick_primes([17,23,9,42]))
# [17, 23]

print(pick_primes([4,2048,100,55]))
# []

