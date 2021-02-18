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
        return 0
    for div in range(2, int(math.sqrt(num)) + 1):
        if num % div == 0:
            return 0
    return 1


def main():
    # [입력] 테스트케이스 입력
    num = int(sys.stdin.readline().strip())
    
    # [for] 소수 모두 구하기, prime의 첫번째 값은 0이므로 False다. (try3)
    prime = [0]
    for check in range(1, 123456*2+1):  # 입력값의 최대가 123456이므로 검사해야하는 소수의 범위는 그 두배까지다
        if isPrime(check):
            prime.append(1)
        else:
            prime.append(0)

    # 테스트케이스 별 베르트랑 공준 확인
    while num != 0:
        # [출력] count 사용 (try 2)
        print(sum(prime[num+1 : num*2+1]))

        # [입력] 다음 테스트케이스 입력
        num = int(sys.stdin.readline().strip())

if __name__ == '__main__':
    main()

# ---------------------------------
# try 3
# 시간을 줄이려고 고민하던 중 다음 질문 (https://www.acmicpc.net/board/view/60204) 확인
# 소수를 미리 구한 후에 count로 그 개수만 계산하는게 반복작업을 줄이므로 효율적이다.