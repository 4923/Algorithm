# [IMPORT MODULE]
import sys

# [INPUT]
n, m = map(int, sys.stdin.readline().strip().split())  # n : vertex, m: edge
# output 없어서 고생하던 문제와 비슷하게 graph를 0으로 채워놓고 하단 dfs 함수에서 배열을 입력받는다.
graph = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

# [VISITED]
visited = [False for _ in range(0, n)]  # change to True if vertex is visited
vertex_cnt = 0

# [DFS]
def DFS(vertex):
    global vertex_cnt
    global visited

    for curr_v in range(1, n+1): # range(n)이 아니라 range(1, n+1)
        # print(f'curr_v: {curr_v}')
        # print(graph[vertex][2])
        # print(f'[Check index error] : {graph[vertex][curr_v]}')  # When curr_v == 2 (out of range)
        # print(f'[Check index error] : {visited[curr_v]}')

        if graph[vertex][curr_v] and not visited[curr_v]:  # 1 -> 2, 2 -> 3 ...
            visited[curr_v] = True
            # vertex_cnt 추가해야함
            vertex_cnt += 1
            DFS(curr_v)

# [Main]
def main():

    # [**input**] : 여길 이렇게 하는구나... 
    for i in range(m):
        v1, v2 = tuple(map(int, input().split()))
        # 양방향 그래프이기 때문에 각 정점에 대한 간선을 각각 저장
        graph[v1][v2] = 1
        graph[v2][v1] = 1
        # print(f'Graph:\n {graph}\n')

    # [ROOT]
    # root_v = 1
    # print(f'root_v: {root_v}')
    visited[1] = True
    DFS(1)  # resursion start

    print(vertex_cnt)

if __name__ == '__main__':
    main()