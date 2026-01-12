def solution(slice, n):
    # 피자 판 수를 1판부터 시작합니다.
    answer = 1
    
    # (피자 판 수 * 조각 수)가 사람 수(n)보다 적은 동안 계속 반복합니다.
    while (answer * slice) < n:
        # 한 판을 더 추가합니다.
        answer += 1
        
    return answer