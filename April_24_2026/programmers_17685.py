# https://school.programmers.co.kr/learn/courses/30/lessons/17685
# 2018 KAKAO BLIND RECRUITMENT
# [3차] 자동완성
#

# 사전순 정리 = 정렬 후 좌우 단어와 비교!!!

def compare(w, w1):
    unique = 0
    min_len = min(len(w), len(w1))
    
    for i in range(min_len):
        if w[i] != w1[i]:
            unique = w[:i+1]
            break

    if not unique:
        unique = w[:min_len+1]
        
    return unique
    

def solution(words):
    words.sort()
    answer = 0

    for idx, w in enumerate(words):
        checklist = []
        
        if idx > 0:
            checklist.append(words[idx -1])
        if idx < len(words)-1:
            checklist.append(words[idx +1])
        
        unique = []
        for word in checklist:
            unique.append(compare(w, word))
        
        if unique: answer += max(map(len, unique))
        #unique = sorted(unique, key=len, reverse=True)
        #print(unique[0])
        
        
    return answer
