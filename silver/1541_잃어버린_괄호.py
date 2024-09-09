# https://www.acmicpc.net/problem/1541
# 1541: 잃어버린 괄호
# 실버2: 수학, 그리디, 문자열, 파싱
# 31120KB 36ms 559B

sic = input()
nums = []
pm = []
tmp = ''
narr = []

for i in sic:
    if i == '+':
        if tmp:
            nums.append(int(tmp))
            tmp = ''
        pm.append(i)
    elif i == '-':
        if tmp:
            nums.append(int(tmp))
            tmp = ''
        pm.append(i)
    else:
        tmp += i
if tmp:
    nums.append(int(tmp))

for i in range(len(pm)):
    if pm[i] == '+':
        nums[i+1] += nums[i]
    else:
        narr.append(nums[i])
narr.append(nums[-1])

res = narr[0]
for i in range(1, len(narr)):
    res -= narr[i]

print(res)