import sys
def main():
    input = sys.stdin.readline
    n = int(input())
    *a, = [0]+list(map(int, input().split()))
    m = int(input())
    dp = [0]*(n*2+1)
    for i in range(n*2+1):
        p = q = i//2
        q += i & 1
        while p > 0 and q <= n and a[p] == a[q]:
            p -= 1
            q += 1
        dp[i] = p
    ans = ''
    for _ in range(m):
        s, e = map(int, input().split())
        i = s+e
        ans += '1\n' if dp[i] < s else '0\n'
    print(ans)
main()