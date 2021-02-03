a, b = map(int, input().split())

def GCD(a, b):
    if a < b:
        a, b = b, a
    
    if b == 0:
        return a
    else:
        return GCD(a%b, b)


print(GCD(a,b))