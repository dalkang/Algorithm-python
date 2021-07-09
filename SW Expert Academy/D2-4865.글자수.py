T = int(input())

for t in range(1, T + 1):
    str1 = input()
    str2 = input()
    list_str1 = list(str1)
    maximum = 0

    for alphabet in list_str1:
        if str2.count(alphabet) > maximum:
            maximum = str2.count(alphabet)

    print("#%d %d" % (t, maximum))