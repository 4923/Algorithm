"""
https://www.acmicpc.net/problem/2941

문제
예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다.
따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

크로아티아 알파벳	변경
č	c=
ć	c-
dž	dz=
đ	d-
lj	lj
nj	nj
š	s=
ž	z=
예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 
단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. 
lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.

입력
첫째 줄에 최대 100글자의 단어가 주어진다. 
알파벳 소문자와 '-', '='로만 이루어져 있다.

단어는 크로아티아 알파벳으로 이루어져 있다. 
문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.

출력
입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
"""

# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

import sys

# INPUT
# maximum length: 100, lower alphabets && '-' && '='
# Is neccessary to convert str to list? -> X. Not sure how to slice string
string = sys.stdin.readline().strip()

# if문으로 하나하나 다 무식하게 검색하는건 아닌것같아서 엎음
# string 내장함수를 쓰라는 말 같아서 find, replace, in 사용


def isCroatia(string, croatia, count):

    # 01-28 구글링 후 풀이
    for alpha_C in croatia:
        string = string.replace(alpha_C, "@")
    return len(string)

    # # num = 0  # loop check variable
    # bPoint = 0
    # while bPoint < len(croatia):

    #     # [탐색] 크로아티아 알파벳
    #     for alpha_C in croatia:
    #         # num += 1  # loop check
    #         # print(f'-------------------{num}-------------------')
    #         # [크로아티아 알파벳의 위치 확인]
    #         index = string.find(alpha_C)
    #         # print(index)
    #         # print(type(index))
    #         # print()

    #         leng = len(alpha_C) - 1

    #         # print(f'alpha_C: {alpha_C}')
    #         if string.find(alpha_C) != -1:

    #             # print(f'[ALPHA_C check] ::\
    #                 # {string[string.find(alpha_C) : string.find(alpha_C)+leng+1]}\
    #                 # \n{string[leng:]}')
    #             # print()

    #             # [결과값 계산]
    #             count += 1
    #             # 문자열 전체를 범위로 두고 replace 하면 한번에 하나씩 지워지는게 아니라 전부 지워지므로 인덱스로 접근

    #             # **파이썬의 문자열은 수정이 불가능하다!**
    #             # replace를 쓰려고 해도 string = string 형식을 만들어야하는데 그러느니 슬라이싱 하는게 나음
    #             # string = string[index : index + alpha_len].replace(alpha_C, " ")  # (??)
    #             string = string[:index] + " " + string[index + leng+1:]
    #             # print(f'Changed string: {string}')
    #             # print()

    #         # [중지조건] if bPoint >= len(croatia)
    #         bPoint = 0
    #         for alpha_C in croatia:
    #             if string.find(alpha_C) == -1:
    #                 bPoint += 1
    #                 # print(f'\n\t\tbPoint : {bPoint}\n')

    # # [탐색] 일반 알파벳
    # string = string.replace(" ", "")
    # # print(f'Normal alphabets: {len(string)}')
    # count += len(string)
    # # print(f'Total count: {count}')
    # return count


def main():
    # variable
    croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    count = 0
    # output
    # print(f'Origin string: {string}')
    print(isCroatia(string, croatia, count))


if __name__ == "__main__":
    main()

# 반례 확인
# input : ljes=njak
# output : 8
# answer : 6

# 반례 확인 2 (예제 3)
# input : nljj
# output : 2
# answer : 3
# find와 replace로 문자열에서 크로아티아문자 lj를 제거하면 nj가 남는데 이걸 붙이면 또다른 크로아티아문자가 되므로 중간에 띄어쓰기를 해주고 다시 띄어쓰기를 제거하는 과정이 필요. (일반 알파벳 개수 셀 때)

# 반례 확인 3 (예제 4)
# input c=c=
# output : 1
# answer : 2
# replace 성질 때문인듯: c=와 c=에서 loop가 각각 따로 지워져야하는데 한번에 지워져버림


"""
2021-01-28
replace 쓰는건 맞았는데 아예 안쓰는 문자로 치환하면 섞일일이 없으니 안전함
엄청 쉽게 풀리네... 이전코드는 무슨... 채점 중간도 아니고 채점 시작하자마자 오답으로 걸렸는데 무슨차이인지 모르겠다
"""
