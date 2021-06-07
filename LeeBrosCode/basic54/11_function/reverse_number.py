# 리스트로 접근해서 거꾸로 출력하는 방법 <- 이게 제일 빠르지 않나

n = list(input())


def remove_zero(n):
    if n[-1] == "0":
        n = n[:-1]
        return remove_zero(n)
    else:
        return n


def print_reverse(n):
    # reversed()는 내장함수로 reversed된 값을 반환한다.
    # .reverse(list)는 list의 함수로 반환값이 없다.
    n = "".join(reversed(n))
    print(n)


print_reverse(remove_zero(n))
