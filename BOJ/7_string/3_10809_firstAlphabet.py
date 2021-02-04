# '''
# https://www.acmicpc.net/problem/10809

# 문제
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 
# 알파벳 소문자로만 이루어져 있다.

# 출력
# 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, 
# ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 
# 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.
# '''

# # INPUT
# s = input()  # str, MAX length: 99, all elements are lower alphabets
# # print(ord('a'),ord('z'))  # ASCII lower alphabet: 97:122

# # SOLVE
# result = [-1 for e in range(0,26)]  # Set basic form of result list (len(result): 26)
# for i in range(0, len(s)):
#     # print(s[i], s.index(s[i]))
#     # [IF] s[i] in ascii number is in alphabet range: 
#     if 97 <= ord(s[i]) <= 122:
#         # [NEED] The order of alphabets
#         # [Assign] index of s[i] at result list which index is order of alphabet s[i]
#         # <idea>  ASCII of 1st alphabet 'a' is 97. Thus, substract ASCII of s[i] - 97 will be order of alphabets
#         result[ord(s[i])-97] = s.index(s[i])
#     # [ELSE] s[i] is outside of alphabet ascii range:
#     # [CONTINUE/Assign] remain -1 (initial list elements)
#     else:
#         continue

# # OUTPUT
# for alphabet in result:
#     print(alphabet, end=" ")

# # TestCase
# # Input : baekjoon
# # Output : 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
# # My result : [1, 0, -1, -1, 2, -1, -1, -1, -1, 4, 3, -1, -1, 7, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1]

a=list(map(str,input()))
b=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(len(a)):
    for j in range(len(b)):
        # print(f'i is {i}, j is {j}, a[i] is {a[i]}, b[j] is {b[j]}')
        if a[i]==b[j]:
            b[j] = i
            # print(f'\n\tcheck : a[{i}] == b[{j}] : {a[i]} == {b[j]}\n\tchanged list == {b}\n')
            break

for j in range(len(b)):
    if type(b[j]) != int:
        b[j] = -1

[print(e, end = " ") for e in b]

# AttributeError: 'int' object has no attribute 'isdigit'
# isdigit() works only for strings.
# https://stackoverflow.com/questions/33049167/attributeerror-int-object-has-no-attribute-isdigit0