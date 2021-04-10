# 살펴보기
# 조건 1. 겹치지 않는 2개의 원소가 하나의 그룹을 이루어야 함.
#   ㄴ 그룹을 이루는 방법 : 모든 경우의 수를 고려해야 하나?
# 조건 2. 그룹의 개수 : N, 주어지는 수 : 2 * N개
# 조건 3. 그룹의 원소의 합 중 최댓값이 최소?
#   ㄴ 정렬해서 반으로 나뉘었을 때 큰 값 그룹의 최소값과 작은 값 그룹의 최댓값의 합?


import sys

N = int(sys.stdin.readline().strip())  # 만들어야 하는 그룹의 수
numbers = list(map(int, sys.stdin.readline().strip().split()))  # 2*N의 숫자


# 정렬
numbers.sort()  # O(nlogn)

# 그룹 두개로 나누기 (작은 수, 큰 수)
# 숫자의 개수가 2의 N배수이기 때문에 무조건 짝수임
small = numbers[:len(numbers)//2]
large = numbers[len(numbers)//2:]

sums = []
for index in range(len(numbers)//2):
    small_number = small[-1-index]  # 작은 그룹에서 큰 순서대로 하나씩
    large_number = large[index]  # 큰 그룹에서 작은 순서대로 하나씩
    small_plus_large = small_number + large_number

    # 합이 어떤 수들의 합인지는 중요하지 않다.
    sums.append(small_plus_large)

# 출력
print(max(sums))


# 다시 살펴보기
# 연산을 할 때마다 연산값을 저장할 리스트를 생성하는데 이 문제는 지난 값을 쓰지 않아도 되므로 최댓값만 갱신해도 됨
# 매칭하기 위한 리스트도 나누었는데 인덱스로 접근하는 편이 메모리에도 좋다.