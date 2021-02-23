'''
https://www.acmicpc.net/problem/1085

문제
한수는 지금 (x, y)에 있다. 직사각형의 왼쪽 아래 꼭짓점은 (0, 0)에 있고, 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 x, y, w, h가 주어진다.

출력
첫째 줄에 문제의 정답을 출력한다.
'''

import sys

# 입력
curr_x, curr_y, end_x, end_y = map(int, sys.stdin.readline().strip().split())

# 가로
if curr_x < end_x/2:
    dis_x = curr_x
else:
    dis_x = end_x - curr_x

# 세로
if curr_y < end_y/2:
    dis_y = curr_y
else:
    dis_y = end_y - curr_y

# 총 거리
if dis_x < dis_y:
    distance = dis_x
else:
    distance = dis_y

# 출력
print(distance)


