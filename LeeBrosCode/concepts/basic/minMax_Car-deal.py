import sys

n = int(sys.stdin.readline().strip()) 
prices = list(map(int, sys.stdin.readline().strip().split()))  # n년간 자동차의 가격

benefit = 0
for buy in range(n):
    for sell in range(buy, n):
        if benefit < prices[sell] - prices[buy] :
            benefit = prices[sell] - prices[buy]

print(benefit)