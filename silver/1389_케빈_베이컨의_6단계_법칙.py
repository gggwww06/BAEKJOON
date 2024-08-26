# 1389 케빈 베이컨의 6단계 법칙
# https://www.acmicpc.net/problem/1389
#

def bfs(st):
    q = [st]
    visited = [0]*(M+1)
    while q:
        w = q.pop(0)
        for i in arr[w]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[w]+1
        if not q:
            return max(visited)

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
res = [0, N]
for i in range(N):
    tmp = bfs(i)
    if res[1] > tmp:
        res[0] = i
        res[1] = tmp
print(res[0])