# NamongK_Ntimes.py

import sys

# INPUT
k, n = map(int, sys.stdin.readline().strip().split())
# print(f'k {k} / n {n}, {type(n)}')
selected_nums = []


# 숫자 고르기
def FindPermutation(cnt):
    # print(f'\n\n{cnt} , {type(cnt)}, {cnt == n} \n\n')

    # Print
    if cnt == n:
        # RecursionError: maximum recursion depth exceeded in comparison => line no.26 (cnt + i), not (i)
        for selected_num in selected_nums:
            print(selected_num, end= " ")
        print()
        return

    else:
        # Recursion
        for num in range(1, k+1):  # 1부터 k까지의 수 이므로
            # Condition <- 조건을 어떻게 걸 것인가
            # 두개 이상 뽑았을 때마다: 방금 뽑은 수와 그 전에 뽑은 수가 같다면 다음 loop로
            if cnt >= 2 and num == selected_nums[-1] and num == selected_nums[-2]:
                continue
            else: 
            # 조건이 없이 뽑을때와 같음. append -> recursion -> pop
                # print(f'I : {num}')
                selected_nums.append(num)
                FindPermutation(cnt + num)
                selected_nums.pop()


def main():
    # 아직 아무것도 고르지 않았므로 인자로 0을 준다.
    FindPermutation(0)

if __name__ == '__main__':
    main()