import sys

number = int(sys.stdin.readline().strip())

# [출력 값]
cnt = 0

while True:
    # [종료조건]
    if number == 1:
        break
    
    cnt += 1

    # [수 조작]
    if number % 2 == 0:
        number /= 2
    else:
        number = number *3 + 1

print(cnt)