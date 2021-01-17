import sys

# input
# sys.stdin.readline() -> 바로 float 변환 안 됨. 왜?
n = sys.stdin.readline().strip()

# round up to the second digit
n = round(float(n), 2)

# output
# sys.stdout.write() -> str만 출력 가능
print(n)