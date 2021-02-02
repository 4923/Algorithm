import sys

# input
A, B, C = map(int, sys.stdin.readline().strip().split())
# print(f'[INPUT CHECK]\n\tA : {A}, B : {B}, C: {C}')

profit = -A
total = 1
while True:
    # print(f'[VARIABLE CHECK]\n\tA : {A}, B : {B}, C: {C}\n\ttotal : {total}')
    if C <= B:  # 1 / (C - B) < x
        print(-1)
        break
    profit += (C-B)
    # print(f'[ANSWER]\n\ttotal: {total}\n\ttotal: {profit}')
    # output
    if profit > 0:
        print(total)
        break

    total += 1
