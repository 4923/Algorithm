# 살펴보기
# 숫자의 개수 1~100, 격자의 크기 n*n
# 행복한 수열 : 연속하여 m개 이상의 동일한 수가 나오는 수열
# 전체 수열이 n개인 이유 : 가로로 n개 + 세로로 n개 (정방행렬이므로)
# 열탐색하면서 연속되는 수 일경우 cnt += 1씩 추가하는 방식, 열탐색이므로 O(n2)
# => 모든 수에 대해 탐색하는게 아니라! 어떤 수라도 m개 이상 연속한다면 무조건 행복한 수열인것
# 행복한 수열임을 확인했을 때 바로 반복에서 빠져나오게 해야 시간 낭비가 없다.

import sys

# 1. 입력
SIZE, X = map(int, sys.stdin.readline().strip().split())  # n, m
grid = [
    list(map(int, sys.stdin.readline().strip().split()))
    for _ in range(SIZE)
]

# 2. 연속 확인
# 3. 행복한 수열의 개수 확인 (최대 2n개)
def isHappy_row():
    happy = 0
    for row in range(SIZE):
        continued = 0  # 행 탐색을 위해 초기화
        temp = grid[row][0]  # 현재 연속하는 수를 확인하기 위한 변수 (초기값)
        for col in range(SIZE):
            if grid[row][col] == temp: 
                continued += 1
                if continued == X:  # 연속되는 수의 개수가 X개 이상이라면 행복한 수열이므로
                    happy += 1
                    break  # 다음 행 탐색
            else:
                temp = grid[row][col]  # 연속 확인을 위해 값 변경
    return happy
    
def isHappy_col():
    happy = 0
    for col in range(SIZE):
        continued = 0  # 열 탐색을 위해 초기화
        temp = grid[col][0]  # 현재 연속하는 수를 확인하기 위한 변수 (초기값)
        for row in range(SIZE):
            if grid[row][col] == temp: 
                continued += 1
                if continued == X:  # 연속되는 수의 개수가 X개 이상이라면 행복한 수열이므로
                    happy += 1
                    break  # 다음 열 탐색
            else:
                temp = grid[row][col]  # 연속 확인을 위해 값 변경
    return happy
    
# 4. 행복한 수열의 수 출력
print(isHappy_col() + isHappy_row())