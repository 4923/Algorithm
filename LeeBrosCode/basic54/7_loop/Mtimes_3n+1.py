import sys

m = int(sys.stdin.readline().strip())
nums = [int(sys.stdin.readline().strip()) for n in range(m)]

for num in nums:
    cnt = 0
    while True:
        if num == 1:
            print(cnt)
            break
        
        cnt += 1
        
        if num % 2 == 0:  # 짝수
            num /= 2
        else:  # 홀수
            num *= 3
            num += 1