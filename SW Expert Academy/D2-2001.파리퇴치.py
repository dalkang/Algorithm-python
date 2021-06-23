T = int(input())
 
for t in range(T):
    N, M = list(map(int, input().split()))
    Box = [[0 for _ in range(N)] for _ in range(N)]
     
    for f in range(N):
        Box[f] = list(map(int, input().split()))
 
    max_n = 0
    
    for b in range(N-M+1):
        for c in range(N-M+1):
            total = 0
            for d in range(b, b+M):
                for e in range(c, c+M):
                    total += Box[d][e]
            if total > max_n:
                max_n = total
             
    print("#%d %d" % (t+1, max_n))