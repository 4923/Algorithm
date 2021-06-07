# n번째 피보나치 수를 출력하라

# 입력 ( 1<= n <= 45)
n = int(input())


def main():
    # 이게 더 쉬운데 왜... 다른 방법을 먼저 배우지...?
    # 일반적으로 생각하는 피보나치 계산방법

    # 1항과 2항이 1이므로 기본값을 1로 채우고 n까지 for loop 돌려서 리스트 생성
    fibs = [1 for _ in range(n + 1)]

    # 세번째 항부터 연산해야 i-1, i-2 에서 out of range 에러가 발생하지 않음
    for i in range(3, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]

    print(fibs[n])


if __name__ == "__main__":
    main()
