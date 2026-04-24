# https://school.programmers.co.kr/learn/courses/30/lessons/17678
# 2018 KAKAO BLIND RECRUITMENT
# [1차] 셔틀버스

# ---

# 콘은 가능한 한 가장 늦은 시각: 마지막 셔틀을 최대한 막차로 탄다

# 특정 인터벌마다 이벤트가 발생한다 -> 그 이벤트를 기준으로. 이번 셔틀에 타는 크루를 기록한다.
# 크루 기준으로 가면 개판! 남!!

START_TIME = 540        # 09:00

def get_crews(timetable):
    crews = []
    for tt in timetable:
        h, m = map(int, tt.split(":"))
        crews.append(60 * h + m)
    return sorted(crews)

def solution(n, t, m, timetable):    
    crews = get_crews(timetable)    
    shuttles = [[] for _ in range(n)]
    
    curr = 0
    for i in range(len(shuttles)):
        s_time = START_TIME + i * t
        while curr < len(crews) and len(shuttles[i]) < m:
            if crews[curr] <= s_time:
                shuttles[i].append(crews[curr])
                curr += 1
            else:
                break
    
#    print(shuttles)
    
    idx = len(shuttles) -1       # last shuttle
    time = START_TIME + t * idx
    
#    print(idx, len(shuttles[idx]), m)
    if len(shuttles[idx]) >= m:
        time = shuttles[idx][-1] -1
    
#    print(time)
    
    return f"{(time//60):02}:{(time%60):02}"
