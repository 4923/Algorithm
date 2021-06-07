import sys

# input
n = int(sys.stdin.readline().strip())

# output
for i in range(1, n + 1):
    # 수가 3의 배수일 때
    if i >= 3 and i % 3 == 0:
        print(0, end=" ")
    # 십의 자리수가 3배수일 때
    elif i >= 10 and (i // 10) % 3 == 0:
        print(0, end=" ")
    # 일의 자리수가 3배수일 때
    elif i >= 3 and i % 10 != 0 and (i % 10) % 3 == 0:
        # print(0, i)
        print(0, end=" ")
    # 제거하지 않은 숫자 출력
    else:
        print(i, end=" ")
