# https://www.acmicpc.net/problem/4195
# 4195번: 친구 네트워크
# gold 2
# 자료 구조, 해시를 사용한 집합과 맵, 분리 집합

#-----------------------------------------------------------------------#
#-----------------------------------------------------------------------#

# 38% 에러 -> 같은 이름 처리..?

# 이거 continue 대신 break 썼다가 에러남 + RecursionError : 재귀 깊이 초과
# def ffrd(a, fdic, a_set):
#     for i in fdic[a]:
#         if i in a_set:
#             continue
#         else:
#             a_set.add(i)
#             ffrd(i, fdic, a_set)
#     return len(a_set)

    
# 재귀 깊이 초과 사유로 새로 작성
# open으로 풀기 귀찮아보임
# T = int(input())
# for _ in range(T):
#     fdic = {}
#     F = int(input())
#     for i in range(F):
#         # 딕셔너리 만들기
#         a, b = input().split()
#         if a != b:
#             if a in fdic:
#                 fdic[a].add(b)
#             else:
#                 fdic[a] = {b}
#             if b in fdic:
#                 fdic[b].add(a)
#             else:
#                 fdic[b] = {a}
        
#         print(fdic)

#         # 친구 수 세기
#         # 이거 bfs 아냐...? 아님 말고
#         a_set= set()
#         print(ffrd(a, fdic, a_set))

#-----------------------------------------------------------------------#
#-----------------------------------------------------------------------#        

# T = int(input())
# for _ in range(T):
#     fdic = {}
#     F = int(input())
#     l = []
#     for i in range(F):
#         a, b = input().split()
#         idx = -1
#         for j in range(len(l)):
#             l_j = l[j]
#             if (a in l_j) or (b in l_j):
#                 l_j.add(a)
#                 l_j.add(b)
#                 if idx >= 0:
#                     # union
#                     l[idx] |= l.pop(j)
#                     break
#                 else:
#                     idx = j
#         if idx < 0 or l == []:
#             l.append({a, b})
        
#         print(l)
#         print(len(l[idx]))

# 시간초과에서 벗어나지 못 함...

#-----------------------------------------------------------------------#
#-----------------------------------------------------------------------#

# union find 알고리즘^^

# 특정 원소가 속한 집합 찾기
def find_parent(x):
    # 루트 노드가 아니면 루트 노드 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        # return find_parent(parent[x])보다 아래 '경로 압축(path compression)'이 시간복잡도 감소
        parent[x] = find_parent(parent[x])
        return parent[x]
    else:
        return x


# 두 원소가 속한 집합 합치기 : union
def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x != y:
        parent[y] = x
        p_num[x] += p_num[y]


T = int(input())
for _ in range(T):
    F = int(input())
    parent = dict()
    p_num = dict()
    for i in range(F):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            p_num[a] = 1
        if b not in parent:
            parent[b] = b
            p_num[b] = 1
        
        union(a, b)
        print(p_num[find_parent(a)])

# https://www.acmicpc.net/board/view/65195



