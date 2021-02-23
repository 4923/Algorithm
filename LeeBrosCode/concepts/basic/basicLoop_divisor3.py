import sys
import math  # sqrt

def div3(num):
    if num == 1 or pow(num, 2) < start:
        return False

    for div in range(2, num):
        if pow(num, 2) % div == 0:
            return False

    print(f'\tnum**2: {num**2}')
    return True

start, end = map(int, sys.stdin.readline().strip().split())

# 약수가 세개라는건 **소수의** 제곱수라는 것
min = int(math.sqrt(start))
max = int(math.sqrt(end))
result = 0

for num in range(min, max+1):
    if div3(num):
        result += 1

print(result)