# 살펴보기
# 박스를 행렬 A로 생각할 때 박스를 90도 돌리면
# 각각의 열은 Transposed되어 행벡터로 변환된다.
# 따라서 이런 유형의 문제는 격자에서 열을 추출하고 가공할 수 있는지를 묻는 문제라고 할 수 있겠다.


# [import package]
import sys  # 여러 줄로 박스의 값을 입력받아야 하므로 sys 사용

# [input]
box_size = int(sys.stdin.readline().strip())
original_box = [
    list(map(int, sys.stdin.readline().strip().split()))
    for _ in range(box_size)
]

# 열을 추출
new_box = []
for column in range(box_size):
    new_row = []  # 추출한 열을 담을 list (열을 추출해 행으로 변환한다.)
    for row in range(box_size-1, -1, -1):  # 밑에서부터 위로 읽어와야하므로 index를 거꾸로 설정한다.
        new_row.append(original_box[row][column])
    new_box.append(new_row)
    
# [output]
for row in range(box_size):
    [print(new_box[row][column], end = " ") for column in range(box_size)]
    print()