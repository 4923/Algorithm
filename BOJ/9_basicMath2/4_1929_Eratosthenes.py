'''
https://www.acmicpc.net/problem/1929

문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
'''

import sys

# 1. 입력
start, end = map(int, sys.stdin.readline().strip().split())

# 2. 해당 범위 안의 수를 미리 나열한 list 생성
# 이 리스트에서 소수가 아닌 수 (n의 배수) 를 False로 변환한다.
sieve = [i for i in range(start, end)]

# 3. 에라토스테네스의 체: 소수가 아닌 수 제거
# 배수를 지울 때 곱하는 수와 곱해지는 수를 위한 for문을 따로 작성할 필요 없이 sieve의 원소에서 나누면 된다.
# 참고한 질문: (https://www.acmicpc.net/board/view/54480)

for isPrime in sieve:
    # 최대 약수는 sqrt(num) 이하이므로 따로 편의를 위해 변수 생성
    sqrt_num = int(round(isPrime ** (1/2)))

    for num in range(2,  sqrt_num + 1):
        # print(f'isPrime : {isPrime}, num : {num}, sqrt_num : {sqrt_num}')

        if isPrime % num == 0:
            sieve[isPrime-start] = False
            # print(f'\tsievs = {sieve}')
            break

        elif num == sqrt_num:
            print(isPrime)       
            break


# '''
# [참고](https://ko.wikipedia.org/wiki/에라토스테네스의_체)
# def prime_list(n):
#     # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
#     sieve = [True] * n

#     # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
#     m = int(n ** 0.5)
#     for i in range(2, m + 1):
#         if sieve[i] == True:           # i가 소수인 경우
#             for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
#                 sieve[j] = False

#     # 소수 목록 산출
#     return [i for i in range(2, n) if sieve[i] == True]
# '''