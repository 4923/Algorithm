'''
[BFS PseudoCode]

def breadth_first_search(problem):

  # a FIFO open_set
  open_set = Queue()
  # an empty set to maintain visited nodes
  closed_set = set()
  # a dictionary to maintain meta information (used for path formation)
  meta = dict()  # key -> (parent state, action to reach child)

  # initialize
  start = problem.get_start_state()
  meta[start] = (None, None)
  open_set.enqueue(start)

  while not open_set.is_empty():

    parent_state = open_set.dequeue()

    if problem.is_goal(parent_state):
    ...
'''

'''
n * m 크기의 이차원 영역의 좌측 상단에서 출발하여 
우측 하단까지 뱀에게 물리지 않고 탈출하려고 합니다. 
이동을 할 때에는 반드시 상하좌우에 인접한 칸으로만 이동할 수 있으며, 
뱀이 있는 칸으로는 이동을 할 수 없습니다. 
뱀에게 물리지 않고 탈출 가능한 경로가 있는지 여부를 판별하는 코드를 작성해보세요.

입력 형식
첫번째 줄에는 n과 m이 공백을 사이에 두고 주어지고,
두번째 줄부터 (n+1)번째 줄까지는 각 행에 뱀이 없는 경우 1, 
뱀이 있는 경우 0이 입력으로 공백을 사이에 두고 주어집니다. 
시작 칸과 끝 칸에는 뱀이 주어지지 않는다고 가정해도 좋습니다.

2 ≤ n, m ≤ 100
출력 형식
좌측 상단에서 출발하여 우측 하단까지 뱀에게 물리지 않고 탈출 가능한 경로가 있으면 1, 없으면 0을 출력합니다.
'''

# MODULE
import sys  # .stdin.readline()
from collections import deque  # .deque()

# INPUT
n, m = map(int, sys.stdin.readline().strip().split())
grid = [
    list(map(int, sys.stdin.readline().strip().split()))
    for _ in range(n)
]  # grid: 2dim Array

print(f'[Grid Check]\n\t{grid}')

# [Variable]
# x == row (down) / y == col (right)
q = deque()
# visited랑 answer 무식하게 이중루프 안돌아도 되잖아 미친건가
visited = [[-1]*m for _ in range(n)]
answer = [[-1]*m for _ in range(n)]

order = 1

print(f'[Variable Check]\n\tq: {q}\n\tvisited: {visited}\n\tanswer: {answer}\n\torder: {order}')

# bool InRange
# grid 안의 점인가
def IsRange(x, y):
    return 0 <= x <= n and 0 <= y <= m

# bool CanGo
# 인접한 위치로 갈 수 있는가
def CanGo(new_x, new_y):
    if not IsRange(new_x, new_y):  # IsRange가 아니면
        return False
    if visited[new_x][new_y] or grid[new_x][new_y] == 0:  # 이미 방문했거나 뱀이 있는경우(0)
        return False
    return True  # 앞의 두 조건이 아니라면 이동 가능하다.
    

# BFS
# 현재 방문한 위치 가져오기 q가 비어있지 않은게 while의 조건이므로 q의 맨 앞을 가져 올 것.
# 그 점을 기준으로 사방을 확인해야 함. (dx, dy)
# => CanGo가 True이면 visited를 True로 변경
def BFS():

    # dx dy로 방향을 미리 지정함. 두 방향에 대해서 확인 (네 방향에 대해 확인하려면 dx = [1, -1, 0, 0] dy = [0, 0, 1, -1])
    dx = [1, 0]  # 우측
    dy = [0, 1]  # 아래

    # 반복문으로 탐색
    while q: # deque이 비지 않았을 때


    return

# main()
def main():
    # 탈출 가능하면 True 출력
    return

if __name__ == '__main__':
    main()