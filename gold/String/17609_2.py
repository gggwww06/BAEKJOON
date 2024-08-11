# https://www.acmicpc.net/problem/17609
# 17609 회문
# gold 5
# 31120KB 272ms 540B

def pd(arr, a, b):
    res1 = res2 = 0
    i, j = a, b
    while i < j:
        if res1 >= 2:
            res1 = 2
            break
        elif arr[i] != arr[j]:
            res1 += 1
            if arr[i+1] == arr[j]:
                i += 1
            elif arr[i] == arr[j-1]:
                j -= 1
            else:
                res1 += 1
        i += 1
        j -= 1

    i, j = a, b
    while i < j:
        if res2 >= 2:
            res2 = 2
            break
        elif arr[i] != arr[j]:
            res2 += 1
            if arr[i] == arr[j-1]:
                j -= 1
            elif arr[i+1] == arr[j]:
                i += 1
            else:
                res2 += 1
        i += 1
        j -= 1

    return min(res1, res2)

T = int(input())
for _ in range(T):
    arr = input()
    N = len(arr)
    i = res1 = res2 = 0
    j = N-1

    print(pd(arr, i, j))