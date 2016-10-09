from math import factorial
import time


def combination(n,k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))

def foundNonBouncy(limit):
    result = 0
    length = len(str(limit))-1
    for subLength in range(length, 2, -1):
        result += combination(subLength+9, 9)
        result += combination(subLength+8, 8)
        result -= 10
    return result + 99

t1 = time.time()
print("Answer:", foundNonBouncy(10**100))
t2 = time.time()
print("Time (s):", t2-t1)
