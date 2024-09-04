# 1244 스위치 켜고 끄기
# 31120KB 32ms 581B

N = int(input())
arr = [0] + list(map(int, input().split()))
std = int(input())

for _ in range(std):
    mf, num = map(int, input().split())
    if mf == 1:
        for i in range(0, N+1, num):
            arr[i] += 1
    else:
        i = 1
        arr[num] += 1
        while True:
            if 0<num+i<N+1 and 0<num-i<N+1 and (arr[num+i]%2) == (arr[num-i]%2):
                arr[num+i] += 1
                arr[num-i] += 1
                i += 1
            else:
                break

arr = list(map(lambda x: x%2, arr))
for i in range(1, N+1, 20):
     print(*arr[i:i+20])
