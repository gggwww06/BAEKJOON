# https://www.acmicpc.net/problem/17609
# 17609 회문
# gold 5
# 31120KB 272ms 540B

def pd(arr, i, j):
    res = 0
    while i < j:
        if res >= 2:
            return 2
        elif arr[i] != arr[j]:
            res += 1
            if arr[i+1] == arr[j]:
                i += 1
            elif arr[i] == arr[j-1]:
                j -= 1
            else:
                res += 1
        i += 1
        j -= 1
    return res

T = int(input())
for _ in range(T):
    arr = input()
    N = len(arr)
    i = res1 = res2 = 0
    j = N-1

    res1 = pd(arr, i, j)
    res2 = pd(arr[::-1], i, j)

    print(min(res1, res2))