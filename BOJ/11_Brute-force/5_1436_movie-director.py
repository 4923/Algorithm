'''
https://www.acmicpc.net/problem/1436

문제
666은 종말을 나타내는 숫자라고 한다. 따라서, 많은 블록버스터 영화에서는 666이 들어간 제목을 많이 사용한다. 영화감독 숌은 세상의 종말 이라는 시리즈 영화의 감독이다. 조지 루카스는 스타워즈를 만들 때, 스타워즈 1, 스타워즈 2, 스타워즈 3, 스타워즈 4, 스타워즈 5, 스타워즈 6과 같이 이름을 지었고, 피터 잭슨은 반지의 제왕을 만들 때, 반지의 제왕 1, 반지의 제왕 2, 반지의 제왕 3과 같이 영화 제목을 지었다.

하지만 숌은 자신이 조지 루카스와 피터 잭슨을 뛰어넘는다는 것을 보여주기 위해서 영화 제목을 좀 다르게 만들기로 했다.

종말의 숫자란 어떤 수에 6이 적어도 3개이상 연속으로 들어가는 수를 말한다. 제일 작은 종말의 숫자는 666이고, 그 다음으로 큰 수는 1666, 2666, 3666, .... 과 같다.

따라서, 숌은 첫 번째 영화의 제목은 세상의 종말 666, 두 번째 영화의 제목은 세상의 종말 1666 이렇게 이름을 지을 것이다. 일반화해서 생각하면, N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 숫자) 와 같다.

숌이 만든 N번째 영화의 제목에 들어간 숫자를 출력하는 프로그램을 작성하시오. 숌은 이 시리즈를 항상 차례대로 만들고, 다른 영화는 만들지 않는다.

입력
첫째 줄에 숫자 N이 주어진다. N은 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 N번째 영화의 제목에 들어간 수를 출력한다.
'''

import sys 

# 종말의 숫자 : 어떤 수에 적어도 6이 세개 이상, 연속으로 들어가는 수
# N번째 영화의 제목 : N번째로 작은 종말의 숫자 (666, 1666, 2666, 3666 ... ...)
# 목표 : N번째 영화에 들어간 숫자 출력

# 입력 : N은 10,000 보다 작거나 같은 자연수
seriesNum = int(sys.stdin.readline().strip())

# 종말의 수 확인
def isEndNum(number):  # input : list
    cnt = 0
    for digit in number:
        if digit == '6': cnt += 1
        if cnt == 3: return True


# 종말의 수 탐색
def endNum(seriesNum):
    temp, cnt  = 0, 0
    while True:
        cnt += 1
        # 6이 포함된 수가 생길 때 마다, 그 6을 666의 첫 자리로 생각
        if '6' in list(str(cnt)):
            temp += 1
            # N번째 6이 들어간 수일 때
            if temp == seriesNum:
                endNum = list(str(cnt))
                # 종말의 수로 변경 (6을 666으로)
                for idx in range(len(endNum)):
                    if endNum[idx] == '6' and not isEndNum(endNum):
                        endNum.insert(idx+1, '6')
                        endNum.insert(idx+2, '6')
                return ''.join(endNum)

# 출력
print(endNum(seriesNum))

# test code
# for i in range(1, 20):
#     print(f'i : {i}\t, {endNum(i)}')


# try 2
# 13번째에서 6666이 아닌 666666 출력 -> isEndNum으로 첫 6만 666으로 만든다.

# try 3
# Runtime Error (Name Error) -> ? : import sys 안넣어서 발생
# 우선 입력값 3439일때부터 None 출력 -> 3439일 때 출력값 : 999666
# cnt 범위가 10000이기 때문 ? 666으로 안늘리면 3439일 때 출력값 9996

# try 4
# 오답인데 영문을 모르겠음