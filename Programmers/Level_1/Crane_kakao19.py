'''Parameter'''
# board : 격자 상태가 담긴 2차원 배열 (값 : 0~100 정수, 0은 빈칸)
# moves : 크레인을 작동시킬 위치 (크기 : 1 ~ 1000, 값 : board의 가로크기 이하 자연수)

'''Return'''
# 터트린 인형의 개수

'''2차원 배열에 접근할 수 있는가'''
def solution(board, moves):
    basket = [-1]
    answer = 0
    for move in moves:
        move -= 1
        # move
        for ind in range(len(board)):
            doll = board[ind][move]
            if doll != 0:
                board[ind][move] = 0
                break
        # basket : Stack
        if doll == 0: continue
        elif basket[-1] == doll: 
            basket.pop()
            answer += 2
        else: basket.append(doll)
    return answer

# [Log]
# try 1 : 9/11
#   오답 케이스 : 1, 2
#   brute force로 모든 격자 확인
# try 2 : 11/11
#   전부 0일 때 doll이 0으로 설정되어 basket에 0이 추가되는 문제