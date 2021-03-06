"""
https://www.acmicpc.net/problem/1193

문제
무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

1/1	1/2	1/3	1/4	1/5	…
2/1	2/2	2/3	2/4	…	…
3/1	3/2	3/3	…	…	…
4/1	4/2	…	…	…	…
5/1	…	…	…	…	…
…	…	…	…	…	…
이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

출력
첫째 줄에 분수를 출력한다.

# 지그재그라는게 이해가 안가서 검색함 : https://nhs0912.tistory.com/56, https://jaimemin.tistory.com/1037
"""

# 문제가 도대체 무슨 의미인지 모르겠다
# 순서: 1/1 1/2 2/1 3/1 2/2 1/3 1/4 2/3 /32 /41 5/1 4/2 3/3 2/4 1/5... ...

import sys

# [분자와 분모의 합계를 찾는 함수 (x번째 분수)]
# 분자 + 분모: 2, 3, 4, 5... ...
# 분자와 분모의 합은 일정하고 순차적으로 늘어난다.
def num_denominator(x):
    # 재귀는 recursion error 발생해서 폐기
    # if x < sub:
    #     return sub+1
    # else:
    #     return num_denominator(x-sub, sub+1)

    # [for] (분모와 분자가 뒤집힐 때 까지) 한 사이클을 돌아 신경쓰지 않아도 되는 값들은 지운다. 2부터 시작.
    for i in range(1, x + 1):
        if x <= i:
            return i + 1
        else:
            x -= i
            i += 1


# [분수를 출력하는 함수]
# x : 사용자 입력값 (x번째 분수를 구하여라.)
def fraction(x, denominator_plus_numerator):
    # 예외
    if x == 1:
        fraction = "1/1"
        return print(fraction)

    # [for] 앞에서 이미 한 사이클 (ex 1/4 2/3 3/2 4/1) 돈 숫자는 무시함
    for cnt in range(1, denominator_plus_numerator + 1):
        # print(f'x: {x}, denomitor_numerator: {denominator_plus_numerator}, cnt: {cnt}')

        if x < denominator_plus_numerator:
            # fraction : 한 사이클 안의 몇 번째 분수인가
            fraction_num = x
            # print(f'fraction: {fraction_num}, denomitor_numerator: {denominator_plus_numerator}, cnt: {cnt}')

            # 첫번째 분수의 분모 분자 합이 2이므로
            if (denominator_plus_numerator - 1) % 2 != 0:  # 홀수번째면 분자가 오름차순으로 증가
                fraction = f"{denominator_plus_numerator - fraction_num}/{fraction_num}"
                print(fraction)
            else:  # 짝수번째면 분모가 오름차순으로 증가 (홀수일때와 분자 분모 순서 뒤바뀜)
                fraction = f"{fraction_num}/{denominator_plus_numerator - fraction_num}"
                print(fraction)

            break

        x -= cnt
        # print(f'fraction: {x}, denomitor_numerator: {denominator_plus_numerator}, cnt: {cnt}')


def main():
    x = int(sys.stdin.readline().strip())
    denominator_plus_numerator = num_denominator(x)
    # print(denominator_plus_numerator)  # 입력값이 14일 때 6
    fraction(x, denominator_plus_numerator)


if __name__ == "__main__":
    main()


# 반례 목록
# [1] 입력값 10
# 10에서 출력값 0/5가 나옴
# 해결: if x <= cnt를 if x <= denominator_numerator로 변경. cnt는 변하는 값이라 비교대상으로 적합하지 않다.

# [2] 입력값 4, 6
# 모두 출력값 1/3이 나옴. 4의 답은 3/1이어야 함
