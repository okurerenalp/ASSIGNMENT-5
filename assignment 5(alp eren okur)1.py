def check_if_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    for i in range(number): 
        if i == 0 or i == 1:
            pass
        else:
            modulo = number % i
            if modulo == 0:
                return False
    return True
def find_first_20_prime():
    first20Prime = []
    for i in range(100):
        if(check_if_prime(i) == True):
            first20Prime.append(i)
            if(len(first20Prime) == 20):
                break
    return first20Prime
def find_fake_primes(primeNumbers):
    fakePrimeNumbers = []
    for i in range(len(primeNumbers) - 1):
        fakePrimeNumber = primeNumbers[i] * primeNumbers[i + 1]
        fakePrimeNumbers.append(fakePrimeNumber)
    return fakePrimeNumbers
print(find_first_20_prime())
print(find_fake_primes(find_first_20_prime()))
