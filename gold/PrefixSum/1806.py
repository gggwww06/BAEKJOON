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
res = 0     # 최소 길이
st = 0      # 시작 포인터
ss = 0      # 끝 포인터
for ed in range(N):     # index 0부터 N까지 이동 => 끝점
    ss += arr[ed]       # 첫 번째 값 더해줌 -> 합
    
    while ss >= S:      # 합이 S 이상이면
        if res == 0:    # min 때문에 res 값 N으로 초기화
            res = N
        res = min(res, ed-st+1)     # 길이 계산해서 최솟값 갱신
        if st >= ed:    # 시작점이 끝점이랑 겹칠 때 탈출
            break
        ss -= arr[st]   # 시작점 한 칸 이동해보기
        st += 1

print(res)