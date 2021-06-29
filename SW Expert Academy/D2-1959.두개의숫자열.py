T = int(input())
 
for t in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
 
    if N > M:
        longer = N
        long_list = A
        shorter = M
        short_list = B
    else:
        longer = M
        long_list = B
        shorter = N
        short_list = A
     
    max_result = 0
    
    for b in range(longer-shorter+1):
        result = 0
        for d in range(shorter):
            result += long_list[b+d] * short_list[d]
        if result > max_result:
            max_result = result
 
    print("#%d %d" % (t+1, max_result))