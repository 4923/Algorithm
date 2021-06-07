# 1amongK_Ntimes.py

# [Import Module]
import sys

# [INPUT]
# K: 1~4 사이의 숫자
# N: N번 반복 (1~8)
k, n = map(int, sys.stdin.readline().strip().split())

selected_nums = []

# [FUNCTION]
# FindPermutation(cnt) -> kCn : pick k among n (Recursion)
# cnt: count
def FindPermutation(cnt):

    # n개 모두 뽑았을 경우
    if cnt == n:
        for selected_num in selected_nums:
            print(selected_num, end=" ")
        print()
        return

    # Recursion Case
    # 1~ K까지의 각 숫자가 뽑혔을 때의 경우
    # N만큼 for문이 중첩되어야 모든 경우의 수를 파악하는데 어떡하나?
    # 1~K 까지의 수 중 하나를 뽑는것을 FindPermutation(n)으로 삼고 다른 수를 뽑는걸 재귀로 구현

    for i in range(1, k + 1):
        selected_nums.append(i)  # i가 뽑혔으니까
        FindPermutation(cnt + 1)  # 다음 수를 뽑도록 loop
        selected_nums.pop()  # 배열의 가장 마지막 원소 제거 (.append()했던거 .pop()으로 제거)


def main():
    FindPermutation(0)  # 1부터 K까지 1씩 증가


if __name__ == "__main__":
    main()
