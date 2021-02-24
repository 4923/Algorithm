'''
1 (1)
11 = 1 & 1 (2)
12 = 1 & 2 (2)
1121 = 1 & 1, 2 & 1 (4)
122111 = 1 & 1, 2 & 1, 1 & 1 (6)
112213 = (6)
12221131 = (8)
1123123111 = (10)

연속하는 수와 그 수의 개수를 다음 원소로 정한다
'''

N = int(input())

sequences = [ '1' ]

# 수열의 각 항은 연속되는 수(num)와 그 수의 개수(cnt)다.
for ind in range(0, N):
    
    num = sequences[ind]  # str
    leng = len(num)  # int
    
    cnt = 0  # int

    for l in range(leng):
        new_num = num[l]  # str
        print(f'new_num : {new_num}')
        for c in range(l, leng):
            if new_num == num[c]:
                cnt += 1
                print(f'\tcnt : {cnt}')
            else:
                cnt = 0
                continue

            new = new_num + str(cnt)
        sequences.append(new)

print(sequences)