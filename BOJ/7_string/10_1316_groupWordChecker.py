'''
https://www.acmicpc.net/problem/1316

문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 
각 문자가 연속해서 나타나는 경우만을 말한다. 
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, 
kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 
둘째 줄부터 N개의 줄에 단어가 들어온다. 
단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.
'''

import sys

# INPUT
N = int(sys.stdin.readline().strip())  # 1 <= N <= 100
group = [sys.stdin.readline().strip() for _ in range(0, N)]

# SOLVE

# [loop] 각 줄의 str에 접근
for index in range(N):
    string = group[index]
    # 요소 확인
    elements = set(string)

    # 연속 확인
    status = 0

    # [loop] 한 줄의 알파벳에 접근
    for element in elements:
        for alpha in string:
            if alpha == element:
                continue
            else:
                status = 1
                # 어떻게 연속되지 않는단걸 알리지?
            
            
        


# OUTPUT
# print(count)