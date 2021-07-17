def backtrack(a, k, last):
    global cnt

    if k == last:
        cnt += 1
        result = 0
        for i in range(len(powerset)):
            if a[i+1] == True:
                result += powerset[i]

        result_arr.append(result)
 
    else:
        k += 1
        ncandidates = 2
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, last)
 
T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    a = [0 for _ in range(len(H)+1)]
    c = [True, False]
    powerset = H
    result_arr = []
    cnt = 0
     
    backtrack(a, 0, len(H))
     
    minimum = 10000

    for r in range(len(result_arr)):
        minus = result_arr[r] - B
        if result_arr[r] >= B:
            if minimum > minus:
                minimum = minus
                
    print("#%d %d" % (t, minimum))