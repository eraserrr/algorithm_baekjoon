n = int(input())
t = []
for i in range(n):
    t.append(int(input()))

test_max = max(t)
dp = [[0] for _ in range(test_max+1)]
dp[1] = [0,1,0,0]
dp[2] = [0,0,1,0]
dp[3] = [0,1,1,1]
for i in range(4,test_max+1):
    for j in range(1,4):
        dp[i].append(sum(dp[i-j])-dp[i-j][j])

for i in range(n):
    print(sum(dp[t[i]])%1000000009)
