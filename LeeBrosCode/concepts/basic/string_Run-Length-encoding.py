# 살펴보기
# 문자가 몇 번 연속되는지 탐색하고 그 개수를 알파벳과 함께 출력
# 리스트를 두개 만들지 말고 문자연속 하나 끝날 때 마다 출력할 수도 있지만 전체 길이도 출력해야하므로...
# 리스트는 시간낭비가 있으니 문자열을 수정한다면?


import sys

string = sys.stdin.readline().strip() + "_"
# 마지막까지 연속되는 값을 확인하기 위해 임의로 길이를 1 늘렸다.

new_string = ""
temp = string[0]
cnt = 0

for char in string:
    if char == temp:
        cnt += 1  # 개수 추가
    else:
        new_string = new_string + temp + str(cnt)
        temp = char  # 임시로 저장한 문자 교체
        cnt = 1  # 초기화

print(len(new_string))
print(new_string)
