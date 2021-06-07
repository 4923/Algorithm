# 19단 출력

# input : X

# output
for i in range(1, 20):
    for j in range(1, 20, 2):
        # / 왼쪽
        if j % 2 != 0 and j < 19:
            print(f"{i} * {j} = {i*j}", end=" ")
        # / 오른쪽
        if (j + 1) % 2 == 0 and (j + 1) <= 19:
            print(f"/ {i} * {j+1} = {i*(j+1)}")
        # 19를 곱할 때
        if j == 19:
            print(f"{i} * {j} = {i*j}")
