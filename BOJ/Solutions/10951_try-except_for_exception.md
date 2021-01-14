# [10951 A+B-4](https://www.acmicpc.net/problem/10951)

### 문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
### 입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
### 출력
각 테스트 케이스마다 A+B를 출력한다.

<hr>

### 제출 코드
```py
while True:
    try:
        a, b = map(int, input().split())    # INPUT
        print(a+b)  # OUTPUT
    except:
        break
```

### 풀이
두 수를 입력 받고 계산한 값을 출력하는 문제다.
종료조건이나 테스트 케이스의 개수가 정해지지 않아서 반복문에 조건을 달기가 모호하다. 한 줄에 두 수를 입력 받아야 하는데 입력 조건을 만족하지 않으면 바로 에러가 발생하기 때문이다.

이 때 `try-except`를 사용하면 쉽게 풀린다.
`try-except`는 먼저 `try`절의 조건을 실행하고, 에러가 발생했을 때 `except`절의 조건을 수행하는 예외처리 문장이다.

따라서
1. `while True`로 무한하게 테스트 케이스를 입력받는다.
2. `try`절에서 각 테스트 케이스의 입력을 `map(int, input().split())`으로 받는다.
    * `input()`으로 입력받은 값을 띄어쓰기로 구분하여 `.split()`으로 나누고
    * 이를 `int`타입으로 변환하여 각 변수 a, b에 `map`하는 과정이다.
3. 입력이 제대로 되지 않거나 프로그램을 종료할 때 `try`절의 조건에 부합하지 않으므로 에러가 뜬다. 따라서 `except`에서 `break`로 `while`절을 종료한다.