"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("You must not enter a value less than 1")

    list = []
    count = 2

    while len(list) < number_of_primes:
        if isPrime(count):
            list.append(count)
        count += 1

    return list

def isPrime(number):
    if 2 == number:
        return True

    for divide in range(2, number):
        result = float(number / divide)
        if result.is_integer():
            return False

    return True
