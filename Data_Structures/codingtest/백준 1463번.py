num = int(input())

dp = [0,0,1,1]

dp = dp + [0] * (num-3)

if num >= 4:
  for n in range(4,num+1):

    dp[n] = 1 + dp[n-1]

    if n % 2 == 0:
      dp[n] = min(dp[n//2]+1,dp[n])
    
    if n % 3 == 0:
      dp[n] = min(dp[n//3]+1,dp[n])

print(dp[num])