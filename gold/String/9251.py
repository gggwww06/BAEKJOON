# https://www.acmicpc.net/problem/9251
# 9251번: LCS
# gold 5

# 1. 모든 종류의 수열 만들어서 비교하기 -> 에바
# 2. 하나씩 비교하기
# ㄴhttps://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence
# 표(2차원 배열)을 만들면 되는구낭...


# def lcs(s1, s2):
#     m_num = 0
#     for i in range(len(s1)):
#         num = 0
#         word = s1[i]
#         # 붙어 있을 필요 x 건너뛰는 거 추가해야함.
#         while word in s2:
#             num += 1
#             if (i+num) == len(s1):
#                 break
#             word += s1[i+num]
#         print(num)
#         m_num = max(m_num, num)
#     return m_num


seq1, seq2 = open('././input.txt').read().split()
num1, num2 = len(seq1), len(seq2)

lcs_arr = [[0] * (num2+1) for _ in range(num1+1)]

for i in range(num1):
    for j in range(num2):
        if seq1[i] == seq2[j]:
            lcs_arr[i+1][j+1] = lcs_arr[i][j] + 1
        else:
            lcs_arr[i+1][j+1] = max(lcs_arr[i][j+1], lcs_arr[i+1][j])

# [print(i) for i in lcs_arr]
print(lcs_arr[num1][num2])

'''
# 원리는 똑같은데 최대값만 구하면 되기 때문에 앞 배열을 굳이 남겨놓지 않고 업데이트한다.
# 그대로 냅두고 같을 때만 +1

a = input().rstrip()
b = input().rstrip()
n = len(a)
m = len(b)

dp = [0] * 1000

for i in range(n):
    mx = 0
    for j in range(m):
        if mx < dp[j]:
            mx = dp[j]
        elif a[i] == b[j]:
            dp[j] = mx + 1
print(max(dp))
'''

