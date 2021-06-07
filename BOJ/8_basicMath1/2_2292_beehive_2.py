"""
https://www.acmicpc.net/problem/2292

문제
https://www.acmicpc.net/JudgeOnline/upload/201009/3(2).png
위의 그림과 같이 육각형으로 이루어진 벌집이 있다. 
그림에서 보는 바와 같이 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 
1씩 증가하는 번호를 주소로 매길 수 있다. 숫자 N이 주어졌을 때, 
벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 
몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오. 
예를 들면, 13까지는 3개, 58까지는 5개를 지난다.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.

출력
입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.
"""

# 각 방의 범위
# [1] 1
# [2] 2 ~ 7 (6)
# [3] 8 ~ 19 (12) : 1 + 6 + 6 + (1 ~ 12)
# [4] 20 ~ 37 (18) : 1 + 6 + 6 + 6 + (1 ~ 18)
# [5] 38 ~ 61 (24) : 1 + 6 + 6 + 6 + 6 + (1 ~ 24)

# 각 방은 6*(칸) 만큼 커진다.
# -----------------------------

# input
import sys

n = int(sys.stdin.readline().strip())

# variable
cnt = 0
curr = 2 + 6 * cnt

# loop
while True:
    max_num = 6 * cnt

    # print(f'curr: {curr} cnt: {cnt} max_num: {max_num}')

    if n == 1:
        print(1)
        break

    elif n >= curr:
        curr += max_num
        cnt += 1
        continue

    else:
        # print('else')
        print(cnt)
        break
