# 살펴보기
# 격자 크기 : n * m
# 블럭을 놓을 때 블록 안에 적힌 숫자의 합이 최대가 될 때 탐색
# 1. 최대가 되려면 가장 큰 수 주위부터 살펴야한다. : 가장 큰 수를 찾는다.
#   그런데... 16 1 1과 13 12 11 이 있다면 후자의 합이 더 크지 않나?
# 2. 와... 어떡하지 정말 모르겠다 정말 모르겠을땐 해설만 보고 코드를 짜보자...

# Solution => 모든 경우의 수를 구하자는 생각은 했었는데... 그냥 이거일 줄이야

# 입력 / 격자를 입력받으므로 import sys
import sys

n, m = map(int, sys.stdin.readline().strip().split())
grid = [sys.stdin.readline().strip().split() for _ in range(n)]  # n * m 이므로
