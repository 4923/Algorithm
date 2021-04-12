# [INPUT]
# str에서는 sys.stdin.readline()이 형변환때문에 더 번거롭다.
n, q = map(str, input().split())  # n: str / q: request
req =  [int(input()) for _ in range(int(q))]  # req: str type, order list  

# print(f'\n[INPUT CHECK]\nn : str type => {n} \nq : str type => {q} \nreq : list type => {req}\n')

# [Order 1]
# 1. 가장 앞에 있는 문자를 제외한 나머지 문자를 한 칸씩 앞으로 당기고 가장 앞에 있던 문자를 가장 뒤로 옮깁니다.
def order1(n):
    # n[1:] += n[0] => TypeError: 'str' object does not support item assignment
    n = n[1:]+n[0]
    print(n)  # [OUTPUT]
    return n  # return 없으면 => TypeError: 'NoneType' object is not subscriptable

# [Order 2]
# 2. 가장 뒤에 있는 문자를 제외한 나머지 문자를 한 칸씩 뒤로 밀고 가장 뒤에 있던 문자를 가장 앞으로 옮깁니다.
def order2(n):
    n = n[-1] + n[:-1]
    print(n)  # [OUTPUT]
    return n

# [Order 3]
# 3. 문자열을 좌우로 뒤집습니다.
def order3(n):
    n = n[::-1]
    print(n)  # [OUTPUT]
    return n

# [Main]
def main():
    string = n  # n is unbound?
    for i in req:
        if i == 1:
            string = order1(string)

        elif i == 2:
            string = order2(string)
            
        elif i == 3:
            string = order3(string)
            

if __name__ == '__main__':
    main()