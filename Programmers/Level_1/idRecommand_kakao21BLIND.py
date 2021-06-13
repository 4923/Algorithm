# 규칙에 맞지 않는 아이디 입력시 -> 유사하면서 규칙에 맞는 아이디 추천

# RULE
# 3 <= len(id) <= 15
# id : alpha.lower() or -, _, . 
# '.' can not be used at first or last, and continuously

# STEP
# 1. id.lower()
# 2. remove special symbol except - _ .
# 3. remove . placed first or last
# 4. if len(id) == 0: id = 'a'
# 5. if len(id) >= 16: id = id[:15] & '.' check (last)
# 6. if len(id) <= 2: while len(id) == 3: id += id[-1]
    
def step1(new_id):
    new_id = ''.join(new_id).lower()
    return list(new_id)

def step2(new_id):
    answer_id = []
    for ind in range(len(new_id)):
        token = str(new_id[ind])
        if token.isalnum(): answer_id.append(token)
        elif token == '-' or token == '_' or token == '.': answer_id.append(token)
        else: continue
    return answer_id

def step3(new_id):
    answer_id = []
    ind = 0
    while ind < len(new_id) :
        if new_id[ind] == '.':
            ind2 = ind + 1
            while ind2 < len(new_id) :
                if new_id[ind] != new_id[ind2]:
                    break
                else:
                    ind2 += 1
            ind = ind2
            answer_id.append('.')
        else:
            answer_id.append(new_id[ind])
            ind += 1
    return answer_id

def step4(new_id):
    for _ in range(len(new_id)):
        if len(new_id) == 0: new_id = step5(new_id)
        elif new_id[0] != '.' and new_id[-1] != '.': break
        elif new_id[0] == '.': del new_id[0]
        elif new_id[-1] == '.': del new_id[-1]
    return new_id

def step5(new_id):
    if len(new_id) == 0: new_id.append('a')
    return new_id
    
def step6(new_id):
    if len(new_id) >= 16:
        del new_id[15:]
    answer_id = step4(new_id)
    return answer_id

def step7(new_id):
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id.append(new_id[-1])
    return new_id
    
def solution(new_id):
    step1_id = step1(new_id)
    print(f'resut of step 1 : {step1_id}')
    
    step2_id = step2(step1_id)
    print(f'resut of step 2 : {"".join(step2_id)}')
    
    step3_id = step3(step2_id)
    print(f'resut of step 3 : {"".join(step3_id)}')
    
    step4_id = step4(step3_id)
    print(f'resut of step 4 : {"".join(step4_id)}')
    
    step5_id = step5(step4_id)
    print(f'resut of step 5 : {"".join(step5_id)}')
    
    step6_id = step6(step5_id)
    print(f'resut of step 6 : {"".join(step6_id)}')
    
    step7_id = step7(step6_id)
    print(f'resut of step 7 : {"".join(step7_id)}')
    
    answer = ''.join(step7_id)
    
    # answer = ''
    return answer

# Log
# step 3: 연속하는 . 을 삭제하는 과정에서 범위 설정 잘못하여 시간 소모

# Other Solution 
# 아... 이거 정규식 문제구나...
# 그리고 3단계를 '..' -> '.' 으로 바꾸는 방법 고미만 했었는데 저렇게 풀어도 괜찮구나...
# 쓸데없는데 시간을 너무 많이 써버려서 (범위) 우선 연속하는 값 처리하는 방식 다시 정리하고 정규식 공부를 해보자.

# 정규식 풀이
# import re

# def solution(new_id):
#     st = new_id
#     st = st.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)
#     st = re.sub('\.+', '.', st)
#     st = re.sub('^[.]|[.]$', '', st)
#     st = 'a' if len(st) == 0 else st[:15]
#     st = re.sub('^[.]|[.]$', '', st)
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#     return st
