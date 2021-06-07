import sys

n, q = map(int, sys.stdin.readline().strip().split())
numbers = list(map(int, sys.stdin.readline().strip().split()))
req = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(q)]

for i in range(q):

    if req[i][0] == 1:
        print(numbers[req[i][1] - 1])
    elif req[i][0] == 2:
        try:
            index = numbers.index(req[i][1])
            print(index + 1)
        except:
            print(0)
    else:  # 3
        for i in range(req[i][1] - 1, req[i][2]):
            print(numbers[i], end=" ")
        print()
    print("---------------------------------------")
