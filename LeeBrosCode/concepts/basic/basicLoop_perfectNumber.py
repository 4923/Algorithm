'''
완전수 : 자기 자신을 제외한 모든 양의 약수를 더했을 때 자기 자신이 되는 수

예) 6 = 1 + 2 + 3
'''

import sys
import math  # sqrt

def is_perfect(num):
    if sum(find_div(num)) == num:
        return True
    return False

def find_div(num):  # O(n)
    div_list = [1]
    for div in range(2, round(math.sqrt(num))+1):
        if num % div == 0:
            div_list.append(div)
            div_list.append(num/div)
    return div_list

def main():  # O(n^2)
    # [input]
    start, end = map(int, sys.stdin.readline().strip().split())
    

    cnt = 0
    for num in range(start, end):
        if is_perfect(num):
            cnt += 1
        continue

    # [output]
    print(cnt)


if __name__ == '__main__':
    main()
