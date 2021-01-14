'''
https://www.acmicpc.net/problem/1157

문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.
주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
'''

# INPUT
word = input().upper()  # len(word) < 1000000 / UPPER ALPHABETS

# SOLVE
word = list(word)  # To use list function: .count(x)
setWord = list(set(word))  # To remove duplicated alphabets: (program doesn't focused on index)

max = 0
freqA = []
for i in range(0, len(setWord)):
    if max < word.count(setWord[i]):
        max = word.count(setWord[i])  # exchange max count
        freqA = [setWord[i]]  # exchange most frequent alphabet list (len should be 1)
    elif max == word.count(setWord[i]):
        max = word.count(setWord[i])  # exchange max count
        freqA.append(setWord[i])  # append most frequent alphabet list (goes to print("?"))
    else:
        continue

# OUTPUT
# UPPER ALPHABETS
if len(freqA) > 1:
    print("?")
else:
    print(freqA[0])

# TESTCASE
# EXAMPLE 1
# INPUT: Mississipi
# OUTPUT: ?

# EXAMPLE 2
# INPUT: zZa
# OUTPUT: Z

# EXAMPLE 3
# INPUT: baaa
# OUTPUT: A
