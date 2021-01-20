'''
k개 중에 1개를 n번 뽑기
1부터 K 사이의 숫자를 하나 고르는 행위를 N번 반복하여 나올 수 있는 모든 서로 다른 순서쌍을 구해주는 프로그램을 작성해보세요.

예를 들어 K이 3, N이 2인 경우 다음과 같이 9개의 조합이 가능합니다.

1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3

입력 형식
첫째 줄에 K와 N이 공백을 사이에 두고 주어집니다.
1 ≤ K ≤ 4
1 ≤ N ≤ 8

출력 형식
서로 다른 순서쌍의 개수 만큼의 줄에 걸쳐 한 줄에 하나씩 순서쌍의 상태를 공백을 사이에 두고 출력합니다. 이때 앞에서 부터 봤을 때 사전순으로 앞선 순서쌍부터 출력합니다.
'''

import sys

# [INPUT]
# K: 1~K 사이의 숫자
# N: N번 반복
K, N = map(int, sys.stdin.readline().strip().split())

# [FUNCTION]
# FindPermutation(cnt) -> kCn - k중에 N개를 고르는 경우
# cnt: count
def FindPermutation(cnt):
    print('[FUNCTION] FindPermutation')
    if cnt == K:
        Print()
        return

    row = []
    for i in range(1, N+1):  # 1~K 사이의 수를 [N번] 뽑기
        print(f'\t[FOR] i is {i}')
        if cnt == K:
            Print()
            return
        row.append(FindPermutation(i+1))
        cnt += 1
        print(f'\t\tROW is {row}')
    
    

def Print():
    print('[FUNCTION] print')
    return 0

def main():
    answer = []
    FindPermutation(1)  # 1부터 K까지 1씩 증가
    return 0

if __name__ == '__main__':
    main()