from typing import List


def is_prime(integer: int) -> bool:
    """Function to check if an integer is a prime"""
    if integer < 1:
        return False

    for i in range(2, integer):
        if integer % i == 0:
            return False
    return True


def factorize(integer: int) -> List[int]:
    """Function to factorize an integer into prime factors"""
    p = 2
    factors = []
    while True:
        if is_prime(p):
            if integer % p == 0:
                integer = integer // p
                factors.append(p)
                p = 2
            else:
                p += 1
        else:
            p += 1

        if p > integer:
            break

    return factors


print(factorize(20))
