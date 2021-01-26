import sys

# input & variable
num = int(sys.stdin.readline().strip())
result = []

# solve
while num != 0:
    result.append(num)
    num = int(sys.stdin.readline().strip())

# output
for element in result:
    print(element)
