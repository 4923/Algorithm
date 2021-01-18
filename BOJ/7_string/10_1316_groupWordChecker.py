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
N = int(sys.stdin.readline())  # 1 <= N <= 100
group = [sys.stdin.readline().strip() for _ in range(0, N)]

# SOLVE
count = len(group)
for i in range(0, N):
    print(f'[0] word: {group[i]}')
    while len(group[i]) != 0:
        first = group[i][0]
        print(f'\t[1] first alphabet: {first}')
        print(f'\t[1] if condition: {group[i].find(first)}')
        # 첫번째 글자를 찾고 지움
        if group[i].find(first) == 0:
            group[i] = group[i][1:]
            print(f'\t\t[2] new string: {group[i]}')
            
        if group[i].find(first) != -1:
            count -= 1
            print("[X]")
            break

# OUTPUT
print(count)