def solution(d, budget):
    cnt = 0
    sorted_d = sorted(d)

    for i in sorted_d:
        rest = budget - i
        if rest > 0 or rest == 0:
            budget -= i
            cnt += 1
        else:
            break
        
    return cnt