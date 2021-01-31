import sys

# 입력 (1 <= n <= 100)
n = int(sys.stdin.readline().strip())

# 2 행 ~
for i in range(n):
    # 1 행
    if i == 0:
        for j in range(n):
            print(j+1, end= " ")
    
    else:
        # 짝수행
        if i % 2 != 0:
            for j in range(n, 0, -1):
                print(n*i + j, end = " ")

        else:
            for j in range(1, n+1):
                print(n*i +j, end = " ")
    print()

'''
1 2 3 4  # 0
8(4+4) 7(4+3) 6 (4+2) 5 (4+1)  # 1
9(8+1) 10(8+2) 11(8+3) 12 (8+4)  # 2
16(12+4) 15(12+3) 14(12+2) 13(12+1) # 3
'''