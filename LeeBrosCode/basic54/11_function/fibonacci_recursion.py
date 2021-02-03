# n번째 피보나치 수를 출력하라

# 입력 ( 1<= n <= 45)
n = int(input())

# 종료 조건을 어떻게 만들지?
def fib(n):
    if n <= 2:
        return 1

    # 아이게 재귀니까... Backtracking으로 함수 안에 함수를 호출하면 되겠구나
    # 메인 연산이 앞의 두 항을 더하는거니까 앞의 두 항을 함수를 호출해서 구하고 return으로 둘을 합한 값을 넘기면 됨
    return fib(n-2)+fib(n-1)
    

def main():
    print(fib(n))

if __name__ == '__main__':
    main()
