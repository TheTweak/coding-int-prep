'''
A child is running up a staircase with n steps, and can hop either 1, 2, or 3
steps at a time. Count how many possible ways there is to run up the staircase.

dp state:
dp[i] = number of ways to get to step i
dp[0] = 1
dp[1] = dp[0] = 1
dp[2] = dp[1]+dp[0] = 1+1 = 2
dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

__
  |
  ---
    |
    ---
       |
'''

def count_ways(n: int) -> int:
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    for i in range(1, n+1):
        if i-1 >= 0:
            dp[i] += dp[i-1]
        if i-2 >= 0:
            dp[i] += dp[i-2]
        if i-3 >= 0:
            dp[i] += dp[i-3]
    return dp[n]


if __name__ == '__main__':
    print(count_ways(3))