import math

#4.You are given list of numbers separated by spaces. 
# Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
from math import sqrt
print("!!!TASK 4!!!")

def filter_prime(nums):
    primes = []
    isPrime = True
    for num in nums:
        for div in range(2, int(sqrt(num))):
            if num % div == 0:
                isPrime = False
                break
        if isPrime is True:
            primes.append(num)
        isPrime = True
    return primes

nums = list(map(int, input().split()))
print(filter_prime(nums))
