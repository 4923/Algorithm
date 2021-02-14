'''
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
'''


import sys


def main():

    # [입력] request 번째 분수를 구하시오
    request = int(sys.stdin.readline().strip())

    # [풀이]
    # 규칙 1: 분자와 분모의 합 cycle 은 일정하며 2부터 시작한다.
    # 규칙 2: cycle 이 짝수일 때 -> 분모가 1부터 cycle -1 까지 오름차순 / 홀수일때 -> 분자가 같은 범위에서 오름차순 정렬
    # 규칙 3: 분모 또는 분자의 최대값은 cycle -1이다.
    # 규칙 4: request는 1부터 cycle-1의 합보다 크다.
    # 규칙 5: request - '1부터 cycle-1의 합'은 분자와 분모의 차이다.


if __name__ == '__main__':
    main()
