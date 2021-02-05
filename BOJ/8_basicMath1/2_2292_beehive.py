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

# -------------------------------------------------------------------------
# @yun-aha : 사진보다 더 큰 숫자는 안풀림
cnt = 2
a=8
while n>0:
    if n==1:
        cnt=1
        print(cnt)
        break
    elif 1<n<8:
        print(cnt)
        break
    else :
        if n>=a:
            a+=6*cnt
            cnt+=1
            print(f'new a: {a}, cnt: {cnt}')
        else:
            print(cnt)
            break


# -------------------------------------------------------------------------
# 식: 1 + 6 * cnt + (1 ~ 6 * (cnt+1)) <-- (try3) 식 잘못 세운 부분 찾음
# [try 3] 아니면 n에서 cnt * 6을 빼고, 남은 n이 cnt * 6보다 크면 cnt를 증가시키고 작으면 멈춰서 cnt를 구하는 방법?

cnt = 2  # [try 4: 1에서 2로 초기값 교체]

while True:

    # [try 3 - 기준] 각 껍질의 최대값
    # 아... 이거 식을 잘못 세웠음 (상단 참고)
    # max_num = (cnt-1) * 6 + cnt * 6
    max_num = cnt * 6  # [try 4: 식 교체]

    print(f'\t[Check] cnt: {cnt}, max_num: {max_num}')

    # [try 3 - 1] n이 max_num보다 크면 n에서 max_num을 뺌
    # try 2에서 시간 초과였으므로 연산 횟수를 줄이기 위함
    if n > max_num:
        n -= max_num
        print(f'new n: {n}, cnt: {cnt}, max_num: {max_num}')
        cnt += 1

    # [try 3 - 2] n이 max_num보다 작으면 : 해당 껍질 안에 있으면
    else:
        print(f'[else] n: {n}, cnt: {cnt}, max_num: {max_num}')
        print(cnt)
        break

# [try 1] 오답: n에서 빼기 시작하면 안이 아니라 밖에서부터 건너오기 때문에 오답임. 
# [try 3]
# ㄴ 아... 상관 없지 않나 근데...?  어차피 순서가 아니라 개수 찾기인데
# ㄴ 비교대상이 오름차순으로 커져서 안되는건가? 아니 그래도 개수인데?
# 반례 (입력값): 7, 93

# [try 4]
# 반례
'''
57
new a: 20, cnt: 3
new a: 38, cnt: 4
new a: 62, cnt: 5
5
        [Check] cnt: 1, max_num: 6
new n: 51, cnt: 1, max_num: 6
        [Check] cnt: 2, max_num: 18
new n: 33, cnt: 2, max_num: 18
        [Check] cnt: 3, max_num: 30
new n: 3, cnt: 3, max_num: 30
        [Check] cnt: 4, max_num: 42
[else] n: 3, cnt: 4, max_num: 42
4
'''

# 저기 max_num : 30이 끼면 안되는데...

# -------------------------------------------------------------------------

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