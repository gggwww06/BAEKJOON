# 11729 하노이 탑 이동 순서
# https://www.acmicpc.net/problem/11729
# 골드 5 재귀
# 31120KB 800ms 160B

def hano(n, a, b, c):
    if n > 0:
        hano(n-1, a, c, b)
        print(a, c)
        hano(n-1, b, a, c)

N = int(input())
print(2**N - 1)
hano(N, 1, 2, 3)