T = int(input())
 
for t in range(T):
    N = int(input())
    first = 1
 
    for n in range(1, N+1):
        if n != 1 and n % 2 == 0:
            first = first - n
        if n != 1 and n % 2:
            first = first + n
            
    print("#%d %d" % (t+1, first))