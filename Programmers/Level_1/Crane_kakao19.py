'''Parameter'''
# board : 격자 상태가 담긴 2차원 배열 (값 : 0~100 정수, 0은 빈칸)
# moves : 크레인을 작동시킬 위치 (크기 : 1 ~ 1000, 값 : board의 가로크기 이하 자연수)

'''Return'''
# 터트린 인형의 개수

# 문제 의도 : 2차원 배열에 접근할 수 있는가

def solution(board, moves):
    basket = []
    answer = 0
    doll = 0
    for move in moves:
        # print()
        # print(f'Crane moves to position {move}')
        for ind in range(len(board)):
            # print(f'\tFind available column in board')
            doll = board[ind][move-1]
            # print(f'\tDoll number is {doll}')
            if doll != 0: 
                board[ind][move-1] = 0
                break
        
        print()
        # print(f'Current basket : {basket}')
        if len(basket) == 0: basket.append(doll)
        elif basket[-1] == doll: 
            del basket[-1]              
            answer += 2
            # print('POP!')
        else: basket.append(doll)
        # print(f'New basket : {basket}')
        # print(answer)
        # print()
    
    return answer


# [Log]
# try 1 : 9/11
#   오답 케이스 : 1, 2