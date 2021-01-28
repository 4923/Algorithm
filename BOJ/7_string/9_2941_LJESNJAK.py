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

# if문으로 하나하나 다 무식하게 검색하는건 아닌것같아서 엎음
# string 내장함수를 쓰라는 말 같아서 find, replace, in 사용

def isCroatia(string, croatia, count):
    # [탐색] 크로아티아 알파벳
    for alpha_C in croatia:
        if string.find(alpha_C) != -1:
            count += 1
            string = string.replace(alpha_C, "")
    
    # [탐색] 일반 알파벳
    count += len(string)
    return count

def main():
    # variable
    croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    count = 0
    # output
    print(isCroatia(string,croatia, count))


if __name__ == '__main__':
    main()

# 반례 확인
# input : ljes=njak
# output : 8 -> which has to be 6