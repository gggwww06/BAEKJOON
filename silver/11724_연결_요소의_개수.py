# https://www.acmicpc.net/problem/11724
# 연결 요소의 개수
# 실버2 그래프, DFS/BFS
# 126696KB 580ms 464B

# N, M = map(int, input().split())
N, M, *arr = map(int, open('../input.txt').read().split())
lst = [[] for _ in range(N+1)]

for i in range(M):
    # a, b = map(int, input().split())
    a, b = arr[2*i], arr[2*i+1]
    lst[a].append(b)
    lst[b].append(a)

cnt = 0
visited = [0]*(N+1)

for i in range(1, N+1):
    if visited[i]:
        continue
    q = [i]
    while q:
        ni = q.pop()
        for di in lst[ni]:
            if visited[di]:
                continue
            q.append(di)
            visited[di] = 1
    cnt += 1

print(cnt)

'''
union-find로도 풀 수 있음

def solution():
    N, M = map(int, input().split())
    group = [i for i in range(N+1)]
    graph = [[i] for i in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        a = group[u]
        b = group[v]
        if a == b:
            continue
        if a > b:
            a, b = b, a
        graph[a] += graph[b]
        graph[b] = []
        for u in graph[a]:
            group[u] = a
    print(len(set(group))-1)
'''