'''
https://www.acmicpc.net/problem/11653

문제
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

출력
N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.
'''

# [입력]
num = int(input())

# [소인수분해] 재귀
# def factorization(num, divisor):
    # # print(f'num: {num} divisor: {divisor}')

    # # 종료조건
    # if num == 1:
    #     return

    # if num % divisor == 0:
    #     divisors.append(divisor)
    #     return factorization(num//divisor, divisor)
    # else:
    #     return factorization(num, divisor+1)

# [소인수분해] while
def factorization(num, divisor):
    
    while True:
        if num == 1:
            return
            
        else:
            if num % divisor == 0:
                divisors.append(divisor)
                num /= divisor
            else:
                divisor += 1



def main():
    global divisors
    divisors = []

    factorization(num, 2)

    # [출력]
    # 예외
    if num == 1:
        pass
    else:
        # print(divisors)
        [print(divisor) for divisor in divisors]

if __name__ == '__main__':
    main()
