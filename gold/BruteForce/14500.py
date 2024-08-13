# https://www.acmicpc.net/problem/14500
# 14500번 : 테트로미노
# gold 5
# 구현, 브루트포스 알고리즘

# 너무 깊음
# def tetromino(a, b, sq_num, snum, v):
#     if a >= N or b >= M:
#         return 0
#     elif sq_num == 4:
#         return snum
#     elif v[a][b] == 1:
#         tetromino(a+1, b, sq_num, snum, v)
#         tetromino(a, b+1, sq_num, snum, v)
#         tetromino(a-1, b, sq_num, snum, v)
#         tetromino(a, b-1, sq_num, snum, v)
#     else:
#         sq_num += 1
#         snum += arr[a][b]
#         v[a][b] = 1
#         tetromino(a+1, b, sq_num, snum, v)
#         tetromino(a, b+1, sq_num, snum, v)
#         tetromino(a-1, b, sq_num, snum, v)
#         tetromino(a, b-1, sq_num, snum, v)

# 도형 모양 모음 브루트포스(노가다)
# tetromino = [
#     [(0, 1), (0, 2), (0, 3)],   # ㅡ
#     [(1, 0), (2, 0), (3, 0)],   # ㅣ
#     [(0, 1), (1, 0), (1, 1)],   # ㅁ
#     [(1, 0), (1, 1), (2, 1)],   # u
#     [(1, 0), (1, -1), (2, -1)], # n
#     [(0, 1), (-1, 1), (-1, 2)], # s
#     [(0, 1), (1, 1), (1, 2)],   # 2
#     [(1, 0), (2, 0), (2, 1)],   # ㄴ
#     [(1, 0), (2, 0), (2, -1)],  # ㄴ 좌우대칭
#     [(0, 1), (0, 2), (-1, 2)],  # ㅢ
#     [(1, 0), (1, 1), (1, 2)],   # ㅣㅡ
#     [(0, 1), (1, 1), (2, 1)],   # ㄱ
#     [(0, 1), (1, 0), (2, 0)],   # ㅣ-
#     [(1, 0), (0, 1), (0, 2)],   # ㅣㅡ
#     [(0, 1), (0, 2), (1, 2)],   # ㅡㅣ
#     [(0, 1), (0, 2), (1, 1)],   # ㅜ
#     [(-1, 1), (0, 1), (1, 1)],  # ㅓ
#     [(-1, 1), (0, 1), (0, 2)],  # ㅗ
#     [(1, 0), (1, 1), (2, 0)]    # ㅏ 
# ]

# dfs
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def dfs(a, b, cnt, s):
    global res
    if s + (4 - cnt) * mn < res:
        return
    if cnt == 4:
        res = max(res, s)
        return
    for dx, dy in dxy:
        na, nb = a + dx, b + dy
        if 0 <= na < N and 0 <= nb < M:
            tmp = arr[na][nb]
            if cnt == 2:
                arr[na][nb] = 0
                dfs(a, b, cnt+1, s + tmp)
                arr[na][nb] = tmp
            arr[na][nb] = 0
            dfs(na, nb, cnt+1, s + tmp)
            arr[na][nb] = tmp


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
mn = max(map(max, arr))

res = 0
# 노가다용
# for i in range(N):
#     for j in range(M):
#         for k in range(len(tetromino)):
#             s = arr[i][j]
#             for a, b in tetromino[k]:
#                 di = i + a
#                 dj = j + b
#                 if 0 <= di < N and 0 <= dj < M:
#                     s += arr[di][dj]
#                 else:
#                     break
#             else:
#                 res = max(res, s)

# dfs
for i in range(N):
    for j in range(M):
        tmp = arr[i][j]
        arr[i][j] = 0
        dfs(i, j, 1, tmp)
        arr[i][j] = tmp

print(res)