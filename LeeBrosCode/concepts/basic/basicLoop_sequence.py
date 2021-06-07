"""
1 (1)
11 = 1 & 1 (2)
12 = 1 & 2 (2)
1121 = 1 & 1, 2 & 1 (4)
122111 = 1 & 1, 2 & 1, 1 & 1 (6)
112213 = (6)
12221131 = (8)
1123123111 = (10)

연속하는 수와 그 수의 개수를 다음 원소로 정한다
"""

N = int(input()) - 1

sequences = ["1"]

# 수열의 각 항은 연속되는 수(num)와 그 수의 개수(cnt)다.
for ind in range(0, N):

    print(f"\n==============\t{ind}\t==============\n")

    num = sequences[ind]  # str
    leng = len(num)  # int

    new_cnt = 1  # int
    new = ""  # str

    for l in range(leng):
        check_num = num[l]  # str
        print(f"num : {num} check_num : {check_num}")
        for c in range(l + 1, leng):
            if check_num == num[c]:
                new_cnt += 1
                print(f"\tcheck_num : {check_num} new_cnt : {new_cnt}")
            else:
                new += check_num + str(new_cnt)
                new_cnt = 1
                print("\t\tCONTINUE")
                continue

            print("------------------------------")

        new = check_num + str(new_cnt)
        print(f"[new] = {new}")
        new_cnt = 1
    sequences.append(new)
    print(f"[sequences] : {sequences}")
    print("\n======================================\n")

print(sequences)
