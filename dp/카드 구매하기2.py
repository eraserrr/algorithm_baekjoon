N = int(input())
pack = [0] + list(map(int,input().split()))
dp = [0] *(N+1)
dp[1] = pack[1]

for i in range(1, N+1):
    x = []
    for j in range(1, i+1):
        x.append(pack[j] + dp[i-j])
    dp[i] = min(x)

print(dp)
