import sys

n = int(sys.stdin.readline().strip()) 
prices = list(map(int, sys.stdin.readline().strip().split()))  # n년간 자동차의 가격

# Time Complextity : O(N^2)
# benefit = 0
# for buy in range(n):
#     for sell in range(buy, n):
#         if benefit < prices[sell] - prices[buy] :
#             benefit = prices[sell] - prices[buy]

# print(benefit)


# Time Complexity : O(N)
# min, max의 시간복잡도 : O(N)

half = n//2 if n % 2 == 0 else (n+1)//2


# 최소, 최대값이 언제 올 지 모르니 min, max를 이용할 수 없음.
low = min(prices[:half])
high = max(prices[half:])

benefit = high - low
print(benefit) if benefit >= 0 else print(0)
