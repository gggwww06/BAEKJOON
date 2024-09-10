# https://www.acmicpc.net/problem/26260
# 26260: 이가 빠진 이진 트리
# 골드5: 그래프, 정렬, 트리, dfs, 재귀
# 45512KB 156ms 289B

def pst(a, b):
    if a == b:
        print(arr[a], end=' ')
        return
    pst(a, (a + b) // 2 - 1)
    pst((a + b) // 2 + 1, b)
    pst((a + b) // 2, (a + b) // 2)

N = int(input())
arr = list(map(int, input().split()))
X = int(input())

arr[arr.index(-1)] = X
arr.sort()
pst(0, N-1)