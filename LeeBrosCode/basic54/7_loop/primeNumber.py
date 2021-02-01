import sys

# 입력
n = int(sys.stdin.readline().strip())

# 유클리드 호제법 Euclidean-algorithm (a>b)
def GCD(a, b):
    if a < b:
        temp = a
        a = b
        b = temp

    if b == 0:
        return a

    return GCD(b, a%b)

def isPrime(n): 
    result = True

    # 최대공약수가 1이 아닌 수
    for i in range(1, n): # 나뉘는 수
        if GCD(n, i) != 1:
            result = False

    return result

def main():
    for i in range(2, n+1):
        if isPrime(i) == True:
            print(i, end = " ")

if __name__ == '__main__':
    main()
