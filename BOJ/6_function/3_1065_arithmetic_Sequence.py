"""
https://www.acmicpc.net/problem/1065

문제
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
"""

# INPUT
n = int(input())  # 1 <= n <= 1000

# 자릿수 분리: seq(n)
def seq(n):
    seq = []
    while n > 0:
        seq.append(n % 10)
        n = n // 10
    return seq  # list


def main():

    # 범위 : 1 < num <= 99
    if n <= 99:
        return print(n)

    # 범위 : 100 <= num < n
    # 세자리 이상일 때 한수의 총 개수: count
    count = 99
    # 100부터 n까지 하나씩 검사
    for num in range(100, n + 1):
        # num의 자릿수: digits
        digits = len(seq(num))

        # 공차 (+ & -): diff
        diff = seq(num)[0] - seq(num)[1]

        # 공차 검사
        for digit in range(0, digits - 1):
            if diff == seq(num)[digit] - seq(num)[digit + 1]:
                # 모든 자릿수의 차이가 같을 때
                if digit == digits - 2:
                    count += 1
            else:
                break

    # OUTPUT
    return print(count)


if __name__ == "__main__":
    main()
