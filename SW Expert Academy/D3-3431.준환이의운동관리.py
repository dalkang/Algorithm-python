T = int(input())

for t in range(1, T+1):
    print("#%d" % (t), end=' ')
    L, U, X = map(int, input().split())
    
    if X < L:
        print(L-X)
    elif L < X < U:
        print('0')
    elif L < X:
        print('-1')