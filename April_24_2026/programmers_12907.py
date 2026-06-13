# https://school.programmers.co.kr/learn/courses/30/lessons/12907
# 연습문제
# 거스름돈
#

# DP 문제 = 점화식. dp[0] 기반 점화식 구조
def solution(n, money):
    
    # memoization array
    # dp[0] = 0원 거슬러주기 = 안주는 경우의 수 1 뿐
    # [0] * n 하고 1 입력보다 아래 방식이 깔끔
    dp = [1] + [0] * n 
    
    for coin in money:
        # 현재 화폐값 이상의 거스름돈부터 경우의 수 추가 가능
        # n+1 해야 n 케이스까지 포함
        for i in range(coin, n+1):
            # 현재 coin을 마지막으로 사용하는 경우의 수를 추가
            # 코인을 outer loop로 가므로 순서만 다른 조합은 중복집계 X
            dp[i] += dp[i-coin]
            
    return dp[n] % 1000000007
