'''
https://www.acmicpc.net/problem/1929

문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
'''

# False의 활용

# 1. 입력
import sys
start, end = map(int, sys.stdin.readline().strip().split())

# 2. 해당 범위 안의 수를 미리 나열한 list 생성
# 이 리스트에서 소수가 아닌 수 (n의 배수) 를 False로 변환한다.
sieve = [i for i in range(start, end+1)]

# 1은 무조건 소수가 아니므로 예외로 처리한다
if 1 in sieve:
    sieve[0] = False

# 3. 에라토스테네스의 체: 소수가 아닌 수 제거
# 배수를 지울 때 곱하는 수와 곱해지는 수를 위한 for문을 따로 작성할 필요 없이 sieve의 원소에서 나누면 된다.
# 참고한 질문: (https://www.acmicpc.net/board/view/54480)

for isPrime in sieve:

    # (변수) 최대 약수는 sqrt(num) 이하이므로 따로 편의를 위해 변수 생성
    sqrt_num = int(round(isPrime ** (1/2)))
    # print(f' isPrime: {isPrime}, sqrt_num: {sqrt_num}')

    # (범위) 2를 검사할 경우 범위가 2~2가 되므로 sqrt에 1이 아닌 2를 더한다.
    for num in range(2,  sqrt_num + 2):  
        # print(f'\tnum : {num}')

        if isPrime != num and isPrime % num == 0:
            sieve[isPrime-start] = False
            # print(f'\t\tsieve = {sieve}\n')
            break
        
        # (elif) 2를 검사할 경우 sqrt_num은 1이 되므로 출력하지 않고 지나가게 된다. num == isPrime 조건을 추가한다.
        elif num == isPrime or num == sqrt_num:
            print(isPrime)
            # (break) 위에서 범위를 sqrt_num + 2로 정했으므로 3의 경우 num이 3까지 도달하게 된다. 이 때 3이 두 번 출력되므로 break 조건을 건다.
            break

# try 3: 1 ~ 100 까지 소수 정상출력 확인
# try 4: 반례 (1 101) 입력 시 101 출력되지 않음 => 시간초과