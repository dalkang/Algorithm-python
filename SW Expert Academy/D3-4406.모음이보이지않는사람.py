T = int(input())
 
for t in range(1, T+1):
    print("#%d" % (t), end=' ')
    word = input()
    
    for w in word:
        if w != 'a' and w != 'e' and w != 'i' and w != 'o' and w != 'u':
            print(w, end='')
    print()