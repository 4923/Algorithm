# -*- coding: utf-8 -*- 

'''
문제
우현이는 어린 시절, 지구 외의 다른 행성에서도 인류들이 살아갈 수 있는 미래가 오리라 믿었다. 그리고 그가 지구라는 세상에 발을 내려 놓은 지 23년이 지난 지금, 세계 최연소 ASNA 우주 비행사가 되어 새로운 세계에 발을 내려 놓는 영광의 순간을 기다리고 있다.
그가 탑승하게 될 우주선은 Alpha Centauri라는 새로운 인류의 보금자리를 개척하기 위한 대규모 생활 유지 시스템을 탑재하고 있기 때문에, 그 크기와 질량이 엄청난 이유로 최신기술력을 총 동원하여 개발한 공간이동 장치를 탑재하였다. 하지만 이 공간이동 장치는 이동 거리를 급격하게 늘릴 경우 기계에 심각한 결함이 발생하는 단점이 있어서, 이전 작동시기에 k광년을 이동하였을 때는 k-1 , k 혹은 k+1 광년만을 다시 이동할 수 있다. 예를 들어, 이 장치를 처음 작동시킬 경우 -1 , 0 , 1 광년을 이론상 이동할 수 있으나 사실상 음수 혹은 0 거리만큼의 이동은 의미가 없으므로 1 광년을 이동할 수 있으며, 그 다음에는 0 , 1 , 2 광년을 이동할 수 있는 것이다. ( 여기서 다시 2광년을 이동한다면 다음 시기엔 1, 2, 3 광년을 이동할 수 있다. )
김우현은 공간이동 장치 작동시의 에너지 소모가 크다는 점을 잘 알고 있기 때문에 x지점에서 y지점을 향해 최소한의 작동 횟수로 이동하려 한다. 하지만 y지점에 도착해서도 공간 이동장치의 안전성을 위하여 y지점에 도착하기 바로 직전의 이동거리는 반드시 1광년으로 하려 한다.
김우현을 위해 x지점부터 정확히 y지점으로 이동하는데 필요한 공간 이동 장치 작동 횟수의 최솟값을 구하는 프로그램을 작성하라.

입력
입력의 첫 줄에는 테스트케이스의 개수 T가 주어진다. 각각의 테스트 케이스에 대해 현재 위치 x 와 목표 위치 y 가 정수로 주어지며, x는 항상 y보다 작은 값을 갖는다. (0 ≤ x < y < 231)

출력
각 테스트 케이스에 대해 x지점으로부터 y지점까지 정확히 도달하는데 필요한 최소한의 공간이동 장치 작동 횟수를 출력한다.
'''

# 1+2+3+4 ... 만큼 늘려서 가고 남는 거리는 시작할 때 1광년씩 미리 가 둔다 (ex: 13광년은 1 + 1 + 2 + 3 + 3 + 2 + 1)
# 도착할 때 1광년만 이동해야 하므로 이동 거리를 1부터 y/2까지로 잡고 작동 횟수는 2를 곱한다. <- ?

import sys

# # [input]
testcase = int(sys.stdin.readline().strip())



def move(start, end):

    # [변수 설정]
    move_cnt = 0; total = move_cnt

    # minimum move from start to y/2 point
    half_distance = (end - start)//2
    # print(f'half_distance = {half_distance}, move_cnt = {move_cnt}')

    moved_distance = 0
    for l in range(1, half_distance+1):
        moved_distance += l
        move_cnt += 1
        # print(f'\tmoved_distance = {moved_distance} l = {l} move_cnt = {move_cnt}')

        # 더 가야할 거리가 남은 거리보다 크면 move_cnt에 1을 추가한다 (해당 광년만큼 이동할 때 두 번 이동) 
        if half_distance - moved_distance <= l + 1:
            move_cnt += 1
            total = move_cnt * 2
            # print(f'[break] total: {total}', end="\t")
            break
    
    # [절반연산 복구]
    if (end - start) % 2 != 0:
        total += 1  # 맨 마지막에 추가해야 2배할 때 문제 생기지 않음
    
    return total

def main():
    # [loop]
    # each input of tc
    for _ in range(testcase):
        start, end = map(int, sys.stdin.readline().strip().split())


        # [예외] 거리 end - start 가 0~5 일 때:
        if end - start <= 5:
            # [변수 설정] 시작과 끝 1씩 이동하므로 total의 기본값 = 2
            current = 0; total = 2
            for d in range(1, 1 + end - start):
                total += 1
                current += d
                # print(f'total: {total}, d: {d}')
                if end - current > d:
                    # print(f'[break] total: {total}', end="\t")
                    break
            # [예외] 1 1 2 1 로 겹치는 수가 있는데 절반 자르면 애매해지는 거리 5 예외처리
            if end - start == 5:
                total += 1
        
        # [일반] 거리 절반 잘라 작동횟수 계산
        else:
            total = move(start, end)

        # [출력]
        # print(f'total: {total}')
        # print('==================================\n')
        print(total)


if __name__ == '__main__':
    main()

# sum = 0
# for i in range(10):
#     sum += i
#     print(f'sum: {sum}, i : {i}')

# sum: 1 = 1
# sum: 3 = 1 + 2
# sum: 6 = 3 + 3
# sum: 10 = 6 + 4
# sum: 15 = 6 + 5
# sum: 21 = 15 + 6
# sum: 28 = 21 + 7
# sum: 36 = 28 + 8
# sum: 45 : 36 + 9
