'''
Given an inf. number of coins: 25, 10, 5, 1 calculate a number of ways to represent N cents.

1) Greedy algorithm

calc_ways(coins, ways, sum)
- if sum == N, ways++ and return
- pick next coin
- if sum + coin <= N, sum += coin
-   calc_ways(coins, ways, sum)
    sum -= coin
- else pick next coin

2) Dynamic programming

with repetitions:

count(N) = count(N-1) + count(1)

count(0) = 1
count(1) = 1
count(2) = count(1) = 1
count(3) = count(2) = 1
count(4) = count(3) = 1
count(5) = count(4) + count(0) = 2
count(6) = count(5) + count(1) = 2 + 1 = 3
count(10) =  

wo repetitions:




'''
import sys


class BruteForceSolution:
    def __init__(self, n):
        self.n = n
        self.coins = [25, 10, 5, 1]
        self.visited = set()

    def __create_cs_key__(self, coin_set: list[int], summ: int) -> str:
        coin_set = sorted(coin_set)
        cs_key = ''.join([str(c) for c in coin_set]) + '_' + str(summ)
        return cs_key

    def __calc_ways__(self, summ: int, coin_set: list[int]) -> int:
        cs_key = self.__create_cs_key__(coin_set, summ)

        if cs_key in self.visited:
            return 0

        self.visited.add(cs_key)

        if summ == self.n:
            #print(coin_set)
            return 1

        result = 0
        for c in self.coins:
            if summ + c <= self.n:
                coin_set.append(c)
                result += self.__calc_ways__(summ + c, coin_set)
                coin_set.pop()

        return result

    def solve(self):
        return self.__calc_ways__(0, [])


class DPSolution:
    def __init__(self, n):
        self.n = n
        self.coins = [1, 2, 5]
        self.dp = [[0 for _ in range(len(self.coins))] for _ in range(n+1)]
        self.dp[0][0] = 1

    def solve(self):
        for i in range(1, self.n + 1):
            for j in range(len(self.coins)):
                c = self.coins[j]
                if i-c >= 0:
                    #print(f'dp[{i}][{j}]=sum(dp[{i-c}][:{j+1}])')
                    self.dp[i][j] = sum(self.dp[i-c][:j+1])

        #for r in self.dp:
        #    print(r)
        return sum(self.dp[self.n])


if __name__ == '__main__':
    print(DPSolution(int(sys.argv[1])).solve())






