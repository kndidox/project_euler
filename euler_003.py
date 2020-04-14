"""
    003-Mayor factor primo

    Los factores primos de 13195 son 5, 7, 13, 29.

    Cual es el mayor factor primo del numero 600851475143 ?

    El teorema fundamental de la aritmetica dice que, cualquier entero positivo es:
    - un numero primo
    - O puede ser formado por un conjunto de factores primos donde f_1 puede repetirse

    8 = 2 * 2 * 2 
    9 =  3 * 3
    15 = 3 * 5
    24 = 2 * 2 * 2 * 3
    11 = 11  

"""
# 
# Solution to Project Euler problem 3
# Copyright (c) Project Nayuki. All rights reserved.
# 
# https://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
# 

import math


# By the fundamental theorem of arithmetic, every integer n > 1 has a unique factorization as a product of prime numbers.
# In other words, the theorem says that n = p_0 * p_1 * ... * p_{m-1}, where each p_i > 1 is prime but not necessarily unique.
# Now if we take the number n and repeatedly divide out its smallest factor (which must also be prime), then the last
# factor that we divide out must be the largest prime factor of n. For reference, 600851475143 = 71 * 839 * 1471 * 6857.
def compute():
    n = 600851475143
    while True:
        p = smallest_prime_factor(n)
        if p < n:
            n //= p
        else:
            return str(n)

# Returns the smallest factor of n, which is in the range [2, n]. The result is always prime.
def smallest_prime_factor(n):
    assert n >= 2
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n  # n itself is prime


if __name__ == "__main__":
    res = compute()

    
    assert 6857 == res
    print("Prueba exitosa")
