'''
최고의 33위치
N * N 크기의 격자 정보가 주어집니다. 
이때 해당 위치에 동전이 있다면 1, 없다면 0이 주어집니다. 
N * N 격자를 벗어나지 않도록 3 * 3 크기의 격자를 적절하게 잘 잡아서 
해당 범위 안에 들어있는 동전의 개수를 최대로 하는 프로그램을 작성해보세요.

입력 형식
첫 번째 줄에는 격자의 크기를 나타내는 N이 주어집니다.
두 번째 줄부터는 N개의 줄에 걸쳐 격자에 대한 정보가 주어집니다. 
각 줄에는 각각의 행에 대한 정보가 주어지며, 
이 정보는 0또는 1로 이루어진 N개의 숫자로 나타내어지며 공백을 사이에 두고 주어집니다.

3 ≤ N ≤ 20

출력 형식
N * N 격자를 벗어나지 않으면서, 3 * 3 크기 격자 내에 들어올 수 있는 최대 동전의 수를 출력해주세요.
'''

import sys

# [INPUT]
# line 1: N for N * N
N = int(sys.stdin.readline().strip())
# line 2 : info of N * N
shape = []
for _ in range(0, N):
    shape.append([int(e) for e in sys.stdin.readline().strip().split()])

print(shape)

# # [SIMULATION]
# # cnt : coin count
# cnt = 0
# cnt_li = []
# for index, row in enumerate (shape):
#     print(f'\t[CHECK] row : {row} / [index] : {index}')
#     for index2, element in enumerate (row):
#         print(f'\t[CHECK] elements of each row : {element} / [index2] : {index2}')
#         if element == 1:
#             cnt += 1
#         if index2 + 2 > N:
#             break

#     if index + 2 >  N:
#         break
# print(f'var cnt : {cnt}')


# cnt = 0  # temp summation
# MAX = cnt  # result
# 
# for i in range(0, N):  # col
#     for j in range(0, 3):  # row
#         print(f'1. [Check] : i is {i}, j is {j} AND current grid is {shape[i][j]} which is shape{i}{j}')
#         if j + i == N:
#             print(f'\t1-1. [CNT check] : cnt is {cnt} and soon reset to 0')
#             cnt = 0
#             break
#         elif shape [i][j] == 1:
#             cnt += 1  # if grid is 1, plus 1 to variable cnt
#             print(f'\t1-2. [CNT change] : plus 1 to cnt, which result in {cnt}')
    
#     if MAX < cnt:
#         MAX = cnt  # change MAXimum
#         print(f'2. [CHANGE MAX] MAX : {MAX}')
#         cnt = 0  # reset variable cnt
# 
# print(f'\n[FINAL] MAX is {MAX}')


# cnt = 0  # temp summation
# MAX = cnt  # result
# 
# for k in range(0, N):  # whole square
#     print(f'0 [Pre Check] : k is {k}, range of i')
#     for i in range(k, N):  # col
#         for j in range(3):  # row
#             print(f'1. [Check] : i is {i}, j is {j} AND current grid is {shape[i][j]} which is shape{i}{j}')
#             if j + i > N:
#                 print(f'\t1-1. [CNT check] : cnt is {cnt} and soon reset to 0')
#                 break
#             elif shape [i][j] == 1:
#                 cnt += 1  # if grid is 1, plus 1 to variable cnt
#                 print(f'\t1-2. [CNT change] : plus 1 to cnt, which result in {cnt}')
#     print("\n------------------------------\n")    

#     if MAX < cnt:
#         MAX = cnt  # change MAXimum
#         print(f'2. [CHANGE MAX] MAX : {MAX}')
#         cnt = 0  # reset variable cnt
#     print("\n------------------------------\n")    

# print(f'\n[FINAL] MAX is {MAX}')



cnt = 0  # temp summation
MAX = cnt  # result

for k in range(0, N):
    if k + 2 > N:
        break

    for i in range (k, k+2):  # col
        for j in range (k, k+2):  # row
            print(f'1. [Check] : i is {i}, j is {j} AND current grid is {shape[i][j]} which is shape{i}{j}')
            if shape[i][j] == 1:
                cnt += 1
                print(f'\t1-2. [CNT change] : plus 1 to cnt, which result in {cnt}')
    
    if MAX < cnt:
        MAX = cnt
        cnt = 0

print(f'\n[FINAL] MAX is {MAX}')
