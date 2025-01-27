# https://www.acmicpc.net/problem/16236
# 아기 상어
# 골드3 구현, 그래프, 시뮬레이션, BFS
# 32412KB 40ms 1544B

dxy = [(-1, 0), (0, -1), (0, 1), (1, 0)]
shark = [2, 0, 0]   # 상어 크기, 먹은 먹이 수, 지난 시간

def find_shark():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                return (i, j)

def find_fish(si, sj):
    visited = [[0]*N for _ in range(N)]
    visited[si][sj] = 1
    q = [(si, sj, 0)]
    max_sec = N*N
    fishes = []
    while q:
        i, j, sec = q.pop(0)
        for di, dj in dxy:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and sec < max_sec:
                if not arr[ni][nj] or arr[ni][nj] == shark[0]: # 0이거나 물고기의 크기가 상어와 같다면
                    visited[ni][nj] = sec + 1
                    q.append((ni, nj, sec+1))
                elif arr[ni][nj] < shark[0]:
                    fishes.append((ni, nj, sec+1))
                    max_sec = sec + 1
                else:
                    visited[ni][nj] = 1
    if fishes:  # 가장 위, 가장 왼쪽 물고기
        fishes.sort()
        return fishes[0]
    else:
        return (-1, -1, 0)

def go_shark():
    while True:
        si, sj = find_shark()
        fi, fj, sec = find_fish(si, sj)
        if fi == -1:
            return
        arr[si][sj] = 0
        arr[fi][fj] = 9
        shark[1] += 1
        shark[2] += sec
        if shark[0] == shark[1]:
            shark[0] += 1
            shark[1] = 0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
go_shark()
print(shark[2])


# que 대신에 stack(그러나 빼지는 않음) 써서 pop 사용x, visited 2차원 배열 대신에 set에 add 사용
# 30616KB 36ms 1387B
# def find_init_pos(N, M):
#     for i in range(N):
#         for j in range(N):
#             if M[i][j] == 9:
#                 return i, j
#
#
# direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
#
# def search_prey(N, M, size, current_pos):
#     stack, stack_, prey = [current_pos], [], []
#     dist = 0
#     visited = set()
#     while stack and not prey:
#         dist += 1
#         for (x, y) in stack:
#             if (x, y) in visited:
#                 continue
#             visited.add((x, y))
#             for (i, j) in direction:
#                 x_, y_ = x + i, y + j
#                 if (0 <= x_ < N) and (0 <= y_ < N):
#                     if 0 < M[x_][y_] < size:
#                         prey.append((x_, y_))
#                     elif M[x_][y_] == 0 or M[x_][y_] == size:
#                         stack_.append((x_, y_))
#         stack = stack_
#         stack_ = []
#     if prey:
#         prey.sort()
#         return prey[0], dist
#     else:
#         return None, 0
#
#
# def hunt():
#     N = int(input())
#     M = [list(map(int, input().split())) for _ in range(N)]
#     pos = find_init_pos(N, M)
#     M[pos[0]][pos[1]] = 0
#     time, size, eat = 0, 2, 0
#     while True:
#         pos, dist = search_prey(N, M, size, pos)
#         if pos is None:
#             break
#         M[pos[0]][pos[1]] = 0
#         time += dist
#         eat += 1
#         if size == eat:
#             size += 1
#             eat = 0
#     print(time)
#
#
# hunt()