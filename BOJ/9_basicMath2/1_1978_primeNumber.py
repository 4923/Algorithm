'''
https://www.acmicpc.net/problem/1978

문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.
'''

import sys

# [입력]
number = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))

prime_cnt = 0
for number in numbers:
    for num in range(2, number+1):  # 1과 자기 자신으로만 나누어 지는 수
        if num == number:
            prime_cnt += 1
        elif num != 1 and number % num == 0:
            break

# [출력]
print(prime_cnt)