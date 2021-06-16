def solution(x):
    return x % sum([int(digit) for digit in list(str(x))]) == 0