'''
N개의 정점과 M개의 간선으로 이루어진 양방향 그래프가 주어졌을 때, 
1번 정점에서 시작하여 주어진 간선을 따라 이동했을 때 도달 할 수 있는 
서로 다른 정점의 수를 구하는 프로그램을 작성해보세요. 
(여기서 1번 정점 자기 자신에 도달하는 경우는 가지수에서 제외합니다.)

다음 예시에서 1번 정점은 2, 3번 정점과 이어져 있기 때문에 답은 2가 됩니다.
(그래프가 이어져있지는 않다)


입력 형식
첫 번째 줄에는 N과 M이 공백을 사이에 두고 주어지고,
두 번째 줄부터는 M개의 줄에 걸쳐 (x, y)가 공백을 사이에 두고 주어집니다.
(x, y)는 두 정점 x, y 가 연결되어 있음을 의미합니다. 
(x, y) 쌍이 동일한 연결관계가 두 번 이상 주어지는 경우는 없다고 가정해도 좋습니다.

1 ≤ N ≤ 1,000

0 ≤ M ≤ min(10,000 , N*(N-1) / 2)

출력 형식
1번 정점과 연결되어 있는 서로 다른 정점의 수를 출력해주세요.
'''

# [IMPORT MODULE]
import sys

# [INPUT]
n, m = map(int, sys.stdin.readline().strip().split())  # n : vertex, m: edge
vertices = [
    list(map(int, sys.stdin.readline().strip().split()))  # x, y
    for _ in range(0, m)
]

# [VISITED]
visited = [False for _ in range(0, n+1)]  # change to True if vertex is visited

# [DFS]
def DFS(vertex):
    for curr_v in range(n+1):
        
        print(f'curr_v: {curr_v}')
        print(f'[Check index error] : {vertices[vertex][curr_v]}')  # When curr_v == 2 (out of range)
        print(f'[Check index error] : {visited[curr_v]}')

        if vertices[vertex][curr_v] and not visited[curr_v]:  # 1 -> 2, 2 -> 3 ...
            visited[curr_v] = True
            DFS(curr_v)

# [Main]
def main():

    # [Set Initial Graph]
    graph = [ list([0 for _ in range(n+1)]) for _ in range(n+1) ]
    print(f'Graph:\n{graph}')

    # start point, end point는 어떻게?
    # 입력받은 값의 [0]이 start고 [1]이 end인가?
    for row in range(m):
        # for row in range(n):
        start = vertices[row][0]  # start vertex x
        print(f'start: {start}')
        end = vertices[row][1]  # end vertex y
        print(f'end: {end}')

        # ??? Assign vertex 
        graph[start][end] = 1  # example line 1 (1, 2) => graph[1][2]
        graph[end][start] = 1

        print(f'Graph:\n {graph}\n')

    # [ROOT]
    root_v = 1
    print(f'root_v: {root_v}')
    visited[root_v] = True
    DFS(root_v)  # resursion start


if __name__ == '__main__':
    main()

