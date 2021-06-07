# a와 b는 index
# 1: a와 b를 교환
# 2: a를 b로 변경

import sys

# input
string, count = sys.stdin.readline().strip().split()
count = int(count)
question = [sys.stdin.readline().strip().split() for _ in range(count)]

# solve

for q in question:

    order = q[0]

    if order == "1":
        index1 = int(q[1]) - 1
        index2 = int(q[2]) - 1

        # 특정 문자만 교환해야하므로 index로 접근
        string = list(string)

        temp = string[index1]
        string[index1] = string[index2]
        string[index2] = temp

        string = "".join(string)

        # output
        print(string)

    else:  # order == 2
        old = q[1]
        new = q[2]

        temp = string
        string = temp.replace(old, new)
        print(string)
