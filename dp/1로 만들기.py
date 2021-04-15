n = int(input())

dp = [0] * 1000001
dp[2] = 1
dp[3] = 1

for i in range(4, n + 1):
    li = []
    if i % 3 == 0:
        li.append(dp[i // 3])
    if i % 2 == 0:
        li.append(dp[i // 2])
    li.append(dp[i - 1])

    dp[i] = min(li) + 1
print(dp[n])
