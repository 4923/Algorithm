# solution 1
def solution(x, n):
    answer = []
    num = x
    for _ in range(n):
        answer.append(num)
        num += x
    return answer

# solution 2 -> Fail
# fail in testcase #8
# counter case
# when x is 0, Value Error: range() arg 3 must not be zero
def solution(x, n):
    return [num for num in range(x, x*(n+1), x)]

# solution 3 -> solved
# solve counter case of solution 2
def solution(x, n):
    return [x * num for num in range(1, n+1)]
