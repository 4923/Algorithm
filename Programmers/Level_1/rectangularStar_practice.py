rowNum, colNum = map(int, input().strip().split(' '))

for col in range(colNum):
    for row in range(rowNum):
        print("*", end="")
    print()


# log
# 문자열 반복해서 푸는 방법도 있던데 그냥 for문으로 풀었음
