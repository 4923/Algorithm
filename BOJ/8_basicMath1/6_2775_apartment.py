"""
https://www.acmicpc.net/problem/2775

문제
평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.
이 아파트에 거주를 하려면 조건이 있는데, “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 는 계약 조항을 꼭 지키고 들어와야 한다.
아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라. 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

입력
첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다

출력
각각의 Test case에 대해서 해당 집에 거주민 수를 출력하라.
"""

# 수가 작으니까 각 층의 경우의 수 다 만들어도 상관 없을 것 같음
# 규칙: apartment[floor][room] = apartment[floor-1][room] + apartment[floor][room-1]

import sys

for _ in range(int(sys.stdin.readline().strip())):
    floors = int(sys.stdin.readline().strip())  # 행
    rooms = int(sys.stdin.readline().strip())  # 열

    # 아파트 grid 생성: 거주인원
    apartment = [[room for room in range(rooms + 1)] for _ in range(floors + 1)]
    print(apartment)

    # index로 접근
    # floor는 0부터 시작하며 room은 1부터 시작한다.
    # 0층은 호실 번호만큼 거주하므로 제외 (range(1, floors))
    for floor in range(1, floors + 1):
        for room in range(1, rooms + 1):

            # 1호는 모두 한 명씩 거주
            if room == 1:
                apartment[floor][room] = 1

            else:
                apartment[floor][room] = (
                    apartment[floor - 1][room] + apartment[floor][room - 1]
                )
                # print(f'\t apartment[{floor}][{room}]:{apartment[floor][room]}, room number: {room}, floor: {floor}')

    # print('----------------------')
    # for floor in apartment:
    #     for room in floor:
    #         print(room, end = " ")
    #     print('')
    # print('----------------------')

    # [출력]
    print(apartment[floors][rooms])
