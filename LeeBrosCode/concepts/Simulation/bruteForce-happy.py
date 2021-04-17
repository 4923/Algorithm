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

# 2. 연속 확인 => 행, 열을 각각 확인할거라면 연속은 중복되는 작업이니 함수처리하는게 효율적이다.(오답)
def isHappy(seq):
    # 주어진 seq가 행복한 수열인지 판단하는 함수입니다.
    consecutive_count, max_ccnt = 1, 1
    for i in range(1, SIZE):
        if seq[i - 1] == seq[i]:
            consecutive_count += 1
        else:
            consecutive_count = 1
        
        # 반복문이 끝날 때 마다 max 함수를 이용해 현재까지 연속한 수와 최대로 연속되는 수롤 비교함
        # 이렇게 할 수도 있구나...
        max_ccnt = max(max_ccnt, consecutive_count)  
    
    # 최대로 연속한 회수가 m이상이면 true를 반환합니다. 
    return max_ccnt >= X

# 3. 행복한 수열의 개수 확인 (최대 2n개)
def isHappy_row():
    happy = 0
    for row in range(SIZE):
        # print(f'\t{grid[row]}')
        if isHappy(grid[row]):
            happy += 1
            # print(f'\t\t{happy}')
    # print(happy)
    return happy
    
def isHappy_col():
    happy = 0
    # 열탐색할때 이중 포문을 돌려야하는데 이 때 isHappy까지 돌리면 O(n3)이 되므로 주의해야한다. (오답)
    for col in range(SIZE):
        seq = []
        for row in range(SIZE):
            # 열만 모은 리스트를 만들면 O(n2)선에서 해결할 수 있다 (오답)
            seq.append(grid[row][col])
        # print(f'\t{seq}')
        if isHappy(seq):
            happy += 1
            # print(f'\t\t{happy}')
    # print(happy)
    return happy
    
# 4. 행복한 수열의 수 출력
print(isHappy_row() + isHappy_col())


# DEBUGING
# 엄청 큰 격자에서 중복해서 답을 세는것 같은데 나머지 내일 풀어보기 (21-04-16)
# isHappy에서 제대로 행복한 수열을 세지 못했음. 해설 보고 따라했다. 난이도 쉬움인데 뭐 이렇게 어렵지 (21-04-17)