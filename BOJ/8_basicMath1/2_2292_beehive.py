'''
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
'''

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

# 식: 1 + 6 * cnt + (1 ~ 6 * cnt)

# [try 3] 아니면 n에서 cnt * 6을 빼고, 남은 n이 cnt * 6보다 크면

cnt = 0
while True:

    # [try 2 - 기준] 각 껍질의 최대값 ( 1 + cnt * 6 + cnt * 6 )
    max_num = 1 + cnt * 6 * 2

    # [try 2 - 0] 예외 처리
    if n  == 1:
        cnt = 1
        print(cnt)
        break

    # [try 2 - 1] 6*cnt가 n에 가까워지도록 cnt를 증가시키고
    elif n > max_num:
        n -= max_num
        print(f'new n: {n}, cnt: {cnt}, max_num: {max_num}')
        cnt += 1

    # [try 2 - 2] 6*cnt가 n보다 커질땐 아니 이렇게하면 안되는데
    # 최댓값을 생각할거면 n/2나 cnt*6*2를 기준으로 해야할듯
    else:
        print(f'[else] n: {n}, cnt: {cnt}, max_num: {max_num}')
        print(cnt)
        break

# [try 1] 오답: n에서 빼기 시작하면 안이 아니라 밖에서부터 건너오기 때문에 오답임.
# 반례 (입력값): 7, 93

# [반복문]
# # input
# import sys
# n = int(sys.stdin.readline().strip())

# cnt = 0
# status = 1

# while status:

#     max_room_number = 6 * cnt
#     room = 1 + max_room_number
#     for i in range(max_room_number):
#         if room + i == n:
#             print(cnt)
#             status = 0
#             break
            
#     cnt += 1