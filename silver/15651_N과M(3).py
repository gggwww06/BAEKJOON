# https://www.acmicpc.net/problem/15651
# 15651 N과 M(3)
# 실버3 백트래킹
# 31120KB 1756ms 171B

def suyer(lst):
    if len(lst) == M:
        print(*lst)
        return
    for i in range(1, N + 1):
        suyer(lst + [i])

N, M = map(int, input().split())
suyer([])