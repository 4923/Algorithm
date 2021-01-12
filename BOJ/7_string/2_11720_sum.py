'''
https://www.acmicpc.net/problem/11720

문제
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

출력
입력으로 주어진 숫자 N개의 합을 출력한다.

# 정수를 문자열로 입력받는 문제. Python처럼 정수 크기에 제한이 없다면 상관 없으나, 예제 3은 일반적인 정수 자료형에 담기에 너무 크다는 점에 주목합시다.
'''

# 공백 없이 쓰여졌다면 .split()은 사용 할 수 없다.
# loop로 접근해야하나? -> str도 인덱싱 할 수 있는지 묻는 문제인듯

# INPUT
n = int(input())  # 1 <= n <= 100
num = input()

# SOLVE
sum = 0
for i in range(0,n):
    sum += int(num[i])

# OUTPUT
print(sum)