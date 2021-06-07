"""
https://www.acmicpc.net/problem/3009

문제
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

입력
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

출력
직사각형의 네 번째 점의 좌표를 출력한다.
"""

import sys

coordinates = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(3)]

results = []

for c in range(2):
    if coordinates[0][c] == coordinates[1][c]:  # O O X
        results.append(coordinates[2][c])  # X
    elif coordinates[1][c] == coordinates[2][c]:  # O X X
        results.append(coordinates[0][c])  # O
    else:  # O X O
        results.append(coordinates[1][c])  # X

[print(result, end=" ") for result in results]
