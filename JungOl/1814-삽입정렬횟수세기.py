N = int(input())
arr = list(map(int, input().split()))
cnt = 0

for n in range(1, N):
    for i in range(n, 0, -1):
        if arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            cnt += 1
        else:
            break

print(cnt)