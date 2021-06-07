"""
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
"""

import sys

# INPUT
N = int(sys.stdin.readline().strip())  # 1 <= N <= 100
strings = [sys.stdin.readline().strip() for _ in range(0, N)]

# SOLVE

# [output] 결과값
cnt = N

# [loop] 각 줄의 str에 접근
for string in strings:

    # checker : 연속되는 상태일 때 1로 변함
    checker = 1

    while len(string) > 0:
        # .index() 를 사용해서 왼쪽부터 지워나갔을 때 다음 .index() 값이 0이 아니면 그룹 단어가 아님
        check = string[0]

        # print('\nBefore')
        # print('----------------------------------------------------------------------------------------------------')
        # print(f'check: {check}\tindex: {string.find(check)}\t checker status: {checker}')
        # print('----------------------------------------------------------------------------------------------------')

        # 연속이 되든 안되든 왼쪽의 수는 지워나가야함.
        # 연속일경우 연속되는만큼 연속되는 값을 지움. ex) ppy -> py -> y
        # print(f'\torigin string: {string}', end = "\t")
        string = string[1:]
        # print(f'\tchanged string: {string}')

        # print('\nAfter')
        # print('----------------------------------------------------------------------------------------------------')
        # print(f'check: {check}\tindex: {string.find(check)}\t checker status: {checker}')
        # print('----------------------------------------------------------------------------------------------------')

        # [condition 1] 연속하지 않고 다른 위치에 같은 알파벳이 있다면 총 개수 cnt에 포함시키지 않음
        if string.find(check) > 0:
            checker = 0
            # print(f'\t\tchecker turns to 0: string.find(check) is {string.find(check)}')
            break
        else:
            checker = 1

    # print(f'\n************************************ [End loop] ************************************\n')

    # 연속이 종료되면 총 개수 cnt에 1을 더함
    if checker == 0:
        cnt -= 1
        # print('\t\n[IS NOT Group Word] ', cnt, '\n')


# OUTPUT
print(cnt)
