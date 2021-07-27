def solution(s):
    answer = ''
    cnt = 0

    for i in s:
        if i == ' ':
            answer += i
            cnt = 0
        elif cnt % 2:
            answer += i.lower()
            cnt += 1
        else:
            answer += i.upper()
            cnt += 1

    return answer