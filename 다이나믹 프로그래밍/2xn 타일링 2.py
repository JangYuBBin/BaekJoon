# 2xn 타일링 2, 11727번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. dp[i] : 2xi 직사각형을 타일로 채우는 방법의 수
# 3. dp[i] = dp[i - 1] + dp[i - 2] * 2

import sys

n = int(sys.stdin.readline().rstrip())

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1

if n == 1:
    print(dp[1])
    exit()
else:
    pass

for i in range(2, n + 1, 1):
    dp[i] = dp[i - 1] + dp[i - 2] * 2
    dp[i] %= 10_007

print(dp[n])
