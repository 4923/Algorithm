'''
https://www.acmicpc.net/problem/2775

문제
평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.

이 아파트에 거주를 하려면 조건이 있는데, “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 는 계약 조항을 꼭 지키고 들어와야 한다.

아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라. 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

입력
첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다

출력
각각의 Test case에 대해서 해당 집에 거주민 수를 출력하라.
'''

# 규칙 1: 층 수는 신경쓰지 않는다
# 규칙 2: 거리가 같을 때는 층수가 낮은 방을 선호한다.
# => N 모양의 지그재그 순환

import sys  # stdin.readline()

# [입력]
# 1 <= floorNum, roomNum <= 99, 1 <= guestNum <= floorNum * roomNum
testcase = int(sys.stdin.readline().strip())

for _ in range(testcase):
    # [입력]
    floorNum, roomNum, guestNum = map(int, sys.stdin.readline().strip().split())

    # [풀이]
    # [1] 밑에서부터 몇번째 층에 묵을지 계산
    floor = guestNum % floorNum
    # print(f'floor: {floor}')

    # [2] 해당 층의 몇 호실에 묵을지 계산
    room = guestNum // floorNum + 1
    # print(f'room: {room}')

    # [결과]
    # 형변환
    floor = str(floor)
    room = str(room).zfill(2)


    # [출력]
    # N번째 손님에게 배정되어야 하는 방 번호를 한 줄에 하나씩 출력
    print(floor+room)