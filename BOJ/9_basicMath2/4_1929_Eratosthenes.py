'''
https://www.acmicpc.net/problem/1929

문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
'''

# False의 활용, 함수의 활용

# 1. 입력
import sys
start, end = map(int, sys.stdin.readline().strip().split())

# 2. return으로 빠지는게 좋겠어서 함수로 이전의 두번째 for문 변경
def isPrime(num):
    if num == 1:
        # print(f'\t[{num}] return False')
        return False
    
    for check in range(2, int(num ** (1/2)) + 1):
        if num % check == 0:
            # print(f'\t[num: {num}] & [check: {check}] return False')
            return False
    
    # print(f'\t[{num}] return True')
    return True

def main():
    # 3. 체를 만들어서 False로 변환하고 False가 아닌 것만 출력하는것이 번거로워서 소수인것만 출력하도록 함
    for num in range(start, end + 1):
        if isPrime(num):
            # 4. 결과 출력
            print(num)


if __name__ == '__main__':
    main()


# ----------------------------------------------------------
# try 3: 1 ~ 100 까지 소수 정상출력 확인
# try 4: 반례 (1 101) 입력 시 101 출력되지 않음 => 시간초과
# try 5 : for isPrime in sieve 에서 인덱스로 접근방식 바꿈
# try 6 : 함수 사용