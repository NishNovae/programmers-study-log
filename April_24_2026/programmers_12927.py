# https://school.programmers.co.kr/learn/courses/30/lessons/12927
# 연습문제
# 야근 지수

#

# fatigue = sum of [leftover * leftover]
# minimal fatigue by subtracting N hours max as sum

import heapq as hq

def solution(n, works):
    maxheap = [-w for w in works]   # maxheap
    hq.heapify(maxheap)
#    print(maxheap)
        
    for i in range(n):
        tmp = hq.heappop(maxheap)
        if tmp == 0:    # max work == 0 hours ==> all done!
            return 0
    
        hq.heappush(maxheap, tmp+1)     # +1: cause maxheap
#        print(maxheap)
    
    answer = 0
    for element in maxheap:
        answer += element * element
    
    return answer
