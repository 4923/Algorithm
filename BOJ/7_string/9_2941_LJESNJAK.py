'''
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
'''

# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

import sys
# INPUT
# maximum length: 100, lower alphabets && '-' && '='
# Is neccessary to convert str to list? -> X. Not sure how to slice string
string = sys.stdin.readline().strip()

count = 0
n = len(string)-1

status = True
while status:
    if 97 <= ord(string[n]) <= 122 :
        # print(f'0 alphabet: {string[n]}')
        count += 1
        n -= 1

    elif string[n] == '=':
        # print(f'1: {string[n]}, {string[n-1]}, {string[n-2]}')
        if string[n-1] == 'z' and string[n-2] == 'd':
            # print(f'  if: {string[n-1]}')
            count += 1
            n -= 3
        elif string[n-1] == 'c' or 'z' or 's':
            # print(f'  elif {string[n-1]}')
            count += 1
            n -= 2
        else:
            n -= 1
            continue

    elif string[n] == '-':
        # print(f'2: {string[n]}')    
        if string[n-1] == 'c' or 'd':
            count += 1
            n -= 2
        else:
            n -= 1
            continue

    elif string[n] == 'j':
        # print(f'3: {string[n]}')    
        if string[n-1] == 'l' or 'j':
            count += 1
            n -= 2

    # print(f'[COUNT] {count}')

    if n == -1:
        status = False

print(count)

# 반례 확인
# input : ljes=njak
# output : 8 -> which has to be 6