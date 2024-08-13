# https://www.acmicpc.net/problem/1916
# 1916번 : 최소비용 구하기
# gold 5
# 그래프 이론, 데이크스트라, 최단 경로

N = int(input())
M = int(input())
bus = [[] for _ in range(N+1)]
expense = dict()

for i in range(M):
    a, b, m = map(int, input().split())
    bus[a].append(b)
    bus[b].append(a)
    expense[(a,b)] = m

st, ed = map(int, input().split())
