'''
https://www.acmicpc.net/problem/4948

문제
베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.
입력의 마지막에는 0이 주어진다.

출력
각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.
'''

import sys
import math  # sqrt

# 소수 판별
def isPrime(num):
    if num == 1:
        return False
    for div in range(2, int(math.sqrt(num)) + 1):
        if num % div == 0:
            return False
    return True

def main():

    # 테스트케이스 입력
    num = int(sys.stdin.readline().strip())
    
    while num != 0:
        # cnt : 출력할 값, 소수의 개수
        cnt = 0
        for check in range(num, 2 * num + 1):
            if isPrime(check):
                cnt += 1

        # 출력
        # print(f'{num} 보다 크고 {2*num}보다 작거나 같은 소수의 개수: {cnt}')
        print(cnt)

        # 다음 테스트케이스 입력
        num = int(sys.stdin.readline().strip())

if __name__ == '__main__':
    main()