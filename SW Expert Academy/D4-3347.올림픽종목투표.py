T = int(input())
 
for t in range(1, T+1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))
 
    vote = []
    for m in range(len(M_list)):
        for n in range(len(N_list)):
            if N_list[n] <= M_list[m]:
                vote.append(n+1)
                break
     
    vote_dict = {}
    for v in vote:
        vote_dict[v] = vote_dict.get(v, 0) + 1
    result = max(vote_dict.values())
    for key, value in vote_dict.items():
        if value == result:
            print("#%d %d" % (t, key))