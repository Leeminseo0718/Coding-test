def solution(numbers):
    total = 0
    # number에 있는 숫자를 꺼내서 total에 하나씩 더하기
    for num in numbers:
        total += num
    # 총 합을 개수로 나눠 평균값을 구함
    answer = total / len(numbers) 
    return answer