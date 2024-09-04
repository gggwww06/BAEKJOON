# https://www.acmicpc.net/problem/2564
# 경비원
# 실버1 구현, 많은 조건 분기
# 31120KB 32ms 622B

def guri(dir, lg):
    if dir == 1:    # 북
        return lg
    elif dir == 2:  # 남
        return 2 * garo + sero - lg
    elif dir == 3:  # 서
        return 2 * (garo + sero) - lg
    else:           # 동
        return garo + lg

garo, sero = map(int, input().split())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dong = list(map(int, input().split()))

# 0, 0을 기준으로 시계방향 거리 통합 계산
dong = guri(dong[0], dong[1])
res = 0
for x, y in arr:
    g = abs(dong - guri(x, y))
    if g > (garo + sero):
        g = 2 * (garo + sero) - g
    res += g

print(res)
