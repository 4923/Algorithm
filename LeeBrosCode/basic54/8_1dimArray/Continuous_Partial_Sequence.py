import sys

# 입력
n1, n2 = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))
b = list(map(int, sys.stdin.readline().strip().split()))

# 확인
def isContinuous(a, b):
    start = a.index(b[0])

    cnt = -1
    for num in b:
        cnt += 1
        if (a[start+cnt] != num):
            return False
    return True

def main():
    if isContinuous(a,b) == True:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()