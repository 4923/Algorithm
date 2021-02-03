import math  # sqrt

# input
n = int(input())
coordinates = [
    list(map(int, input().split()))
    for _ in range(n)
]

def len(start, end):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    len = math.sqrt(
        math.pow((x2-x1), 2) + math.pow((y2-y1), 2)
        )
    # print(f'\t\tlen: {len}, coordinate: ({x1}, {y1}), ({x2}, {y2})')
    
    return len

def triangle(first, second, third):
    len1 = len(first, second)
    len2 = len(second, third)
    len3 = len(third, first)
    # print(f'\tlen1: {len1}, len2: {len2}, len3: {len3} ==> sum: {len1+len2+len3}')

    return len1 + len2 + len3

def main():
    perimeters = []
    # 만들 수 있는 삼각형의 경우의 수 탐색
    for i in range(n):
        for j in range(i+1, n):
            for l in range(j+1, n):
                # print(f'i: {i}, j: {j}, l: {l}')
                perimeter = triangle(coordinates[i], coordinates[j], coordinates[l])
                # print(f'perimeter: {perimeter}')
                if perimeter != 0:
                    perimeters.append(perimeter)
                    # print(f'[APPEND]: {perimeter}')
    
    perimeters.sort()

    # 최소둘레 출력
    min_len = perimeters[0]
    # print(perimeters)

    print(f'{min_len:.2f}')


if __name__ == "__main__":
    main()

