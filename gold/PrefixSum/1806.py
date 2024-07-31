# https://www.acmicpc.net/problem/1806
# 1806번: 부분합
# gold 4
# 누적 합, 두 포인터

# N, S = map(int, input().split())
# arr = list(map(int, input().split()))

N, S, *arr = map(int, open('././input.txt').read().split())

###########################시간초과###########################
# res = ed = N
# for st in range(N):
#     ss = 0  # 부분합
#     for i in range(st, ed):
#         if (i-st) > res:
#             break
#         ss = sum(arr[st:i])
#         if ss >= S:
#             res = min(res, i-st)
# print(res)
#########################################################

# 누적 합!!!!! 시작포인터(st), 끝포인터(ed)로 끝포인터 이동하면서? 더해가면서 빼주기
res = N
st = 0
ss = 0
for ed in range(N):
    ss += arr[ed]
    
    while ss >= S:
        res = min(res, ed-st+1)
        if ss == S:
            break
        ss -= arr[st]
        st += 1

print(res)