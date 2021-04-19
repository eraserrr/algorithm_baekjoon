n = int(input())

dp = {}
x = []
for i in range(n):
    a = int(input())
    x.append(a)

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,max(x)+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in x:
    print(dp[i])
