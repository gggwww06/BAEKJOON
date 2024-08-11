# https://www.acmicpc.net/problem/2212
# 2212 센서
# gold 5
# 32140KB 36ms 158B

N = int(input())
K = int(input())
arr = sorted(list(map(int, input().split())))

diff = sorted([arr[i+1] - arr[i] for i in range(N-1)])
print(sum(diff[:N-K]))    # [ : -(K-1)] 은 오류발생