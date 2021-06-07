# n번째 피보나치 수를 출력하라

# 입력 ( 1<= n <= 45)
n = int(input())


def fib(n):
    if n <= 2:
        return 1

    # 리스트에 어떻게 저장하냐...
    fibs[n - 1] = fib(n - 2) + fib(n - 1)

    # return fib(n-2)+fib(n-1)  # 이게 아니라
    return fibs[n - 1]  # 이걸 호출해야 함.

    # 뭘 리턴할지 고민이 많았는데 fibs에 함수를 호출해서 재귀를 구현하고 리턴값으로 리스트를 넘기면 중복되는 재귀를 피할 수 있다.


def main():
    global fibs
    fibs = [0 for _ in range(n)]
    print(fib(n))


if __name__ == "__main__":
    main()
