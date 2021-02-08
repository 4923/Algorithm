'''
https://www.acmicpc.net/problem/1193

문제
무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

1/1	1/2	1/3	1/4	1/5	…
2/1	2/2	2/3	2/4	…	…
3/1	3/2	3/3	…	…	…
4/1	4/2	…	…	…	…
5/1	…	…	…	…	…
…	…	…	…	…	…
이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

출력
첫째 줄에 분수를 출력한다.

# 지그재그라는게 이해가 안가서 검색함 : https://nhs0912.tistory.com/56, https://jaimemin.tistory.com/1037
'''

# 문제가 도대체 무슨 의미인지 모르겠다
# 순서: 1/1 1/2 2/1 3/1 2/2 1/3 1/4 2/3 /32 /41 5/1 4/2 3/3 2/4 1/5... ...

import sys

# 분자 + 분모: 2, 3, 4, 5... ...
# 분자와 분모의 합계 찾기: (x번째 분수, 1)
def num_denominator(x, sub):
    # if x < sub:
    #     return sub+1
    # else:
    #     return num_denominator(x-sub, sub+1)
    for i in range(x):
        if x < i:
            return i+1
        else:
            x -= i
            i += 1



def fraction(x, denominator_numerator):

    # 앞에서 이미 한 사이클 (ex 1/4 2/3 3/2 4/1) 돈 숫자는 무시함
    for cnt in range(1, denominator_numerator):
        x -= cnt

        if x <= cnt:
            fraction_num = x
    
            if (denominator_numerator-1) % 2 != 0:  # 홀수번째면 분자가 오름차순으로 증가
                fraction = f'{denominator_numerator - fraction_num}/{fraction_num}'
                print(fraction)
            else:  # 짝수번째면 분모가 오름차순으로 증가 (홀수일때와 분자 분모 순서 뒤바뀜)
                fraction = f'{fraction_num}/{denominator_numerator - fraction_num}'
                print(fraction)
            
            break

def main():
    x = int(sys.stdin.readline().strip())
    denominator_numerator = num_denominator(x, 1)
    # print(denominator_numerator)
    fraction(x, denominator_numerator)


if __name__ == '__main__':
    main()