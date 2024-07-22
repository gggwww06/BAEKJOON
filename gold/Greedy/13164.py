# https://www.acmicpc.net/problem/13164
# 13164번: 행복 유치원
# gold 5

# 각 리스트 간의 차를 구한 후 최댓값을 (k-1)개 제외한 나머지를 더함

# 얘는 괜찮고
n, k, *a = map(int, open('././input.txt').read().split())

# 이거 백준 서버 오류남
# diff = [a[i+1] - a[i] for i in range(n-1)]
# 하나씩 하나씩 추가해줘야한다...
diff = []
for i in range(n-1):
    diff.append(a[i+1] - a[i])
# 이거 귀찮다고 한 줄로 썼다가 오류 10번남ㅋㅋ

print(a)
print(diff)

diff.sort()

print(sum(diff[:-(k-1)]))

