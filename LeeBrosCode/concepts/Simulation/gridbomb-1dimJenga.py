import sys

# input
n = int(sys.stdin.readline().strip())
blocks = [int(sys.stdin.readline().strip()) for _ in range(n)]
s1, e1 = map(int, sys.stdin.readline().strip().split())
s2, e2 = map(int, sys.stdin.readline().strip().split())

# print(f'[INPUT CHECK]\n\tn: {n}\n\tblocks: {blocks}')

# 남아있는 블록의 목록 세로로 출력
def printBlocks(blocks):
    for i in range(len(blocks)):
        print(blocks[i])

# 블록 빼기
def out(start, end, blocks):
    # index 0부터 시작하는데 block는 1부터 시작이므로 1 뺀다.
    start -= 1
    end -= 1
    # print(f'\t[Numbers] : start {start}, end {end}')
    
    if start == end:
        del blocks[start]
    else:
        del blocks[start:end+1]  # range니까 end에 +1 해야 end까지 삭제 됨.
    # print(f'BLOCKS!!!!!! {blocks}')
    return blocks

def main():
    result = out(s1, e1, blocks)
    result = out(s2, e2, result)
    
    # OUTPUT
    print(len(result))
    printBlocks(result)

if __name__ =='__main__':
    main()