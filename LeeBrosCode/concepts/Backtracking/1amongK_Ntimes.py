# [Import Module]
import sys

# [INPUT]
# K: 1~4 사이의 숫자
# N: N번 반복 (1~8)
k, n = map(int, sys.stdin.readline().strip().split())

# [FUNCTION]
# FindPermutation(cnt) -> kCn : pick k among n (Recursion)
# cnt: count
def FindPermutation(cnt):
    
    # Base Case
    if n == 1:
        return n
    
    com = []
    # Recursion Case
    # N만큼 for문이 중첩되어야 모든 경우의 수를 파악하는데 어떡하나?
    # 1~K 까지의 수 중 하나를 뽑는것을 FindPermutation(n)으로 삼고 다른 수를 뽑는걸 재귀로 구현
    



    
    return
    
    

# Print(): for문으로 모든 결과를 출력
def Print():
    print('[FUNCTION] print')

    return 0

def main():
    cnt = 0
    answer = []
    FindPermutation(1)  # 1부터 K까지 1씩 증가
    
    for i in range(n):
        for j in range(k):
            answer.append(FindPermutation(j))
    
    return 0

if __name__ == '__main__':
    main()