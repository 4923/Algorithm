import sys


def main():

    # [입력] 원소의 수
    N = int(sys.stdin.readline().strip())

    numbers = list(map(int, sys.stdin.readline().strip().split()))
    unique = []

    # 중복 확인
    for number in numbers:
        if numbers.count(number) == 1:
            unique.append(number)

    # # [출력] 최대
    if len(unique) != 0:
        print(max(unique))

    # [출력] 최대값이 없을 때 (모두 중복)
    else:
        print(-1)


if __name__ == "__main__":
    main()
