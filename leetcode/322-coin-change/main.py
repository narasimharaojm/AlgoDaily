import sys


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int

        1st approach: top-down bfs + hashtable

        LTE
        """
        hs = set()
        queue = []
        queue.append((amount, 0))
        while len(queue) > 0:
            n = len(queue)
            for i in range(n):
                remain, count = queue.pop(0)
                if remain in hs:
                    continue
                hs.add(remain)
                if remain == 0:
                    return count
                elif remain > 0:
                    for coin in coins:
                        queue.append((remain-coin, count+1))
        return -1


print(Solution().coinChange([5], 5))
print(Solution().coinChange([1, 2, 5], 11))
print(Solution().coinChange([2], 3))
print(Solution().coinChange([1, 7, 11, 13, 17], 152))
print(Solution().coinChange(
    [70, 177, 394, 428, 427, 437, 176, 145, 83, 370], 7582))
print("--------------------")

"""
3rd attempt
learned from others: bottom-up
e.g. coins = [1,2,5], amount = 7
f(0) = 0  so if f(100-100), it output 0+1=1
f(1) = min(f(1)) + 1
f(2) = min(f(1)+f(0)) + 1
f(3) = min(f(2)+f(1)) + 1
f(4) = min(f(3)+f(2)) + 1
f(5) = min(f(4)+f(3)+f(0)) + 1
f(6) = min(f(5)+f(4)+f(1)) + 1
f(7) = min(f(6)+f(5)+f(2)) + 1
...
1300 ms, faster than 31.42%
"""


class Solution(object):
    def coinChange(self, coins, amount):
        dp = (amount+1)*[0]
        for i in range(1, amount+1):
            temp = sys.maxsize
            for coin in coins:
                remain = i-coin
                if remain >= 0:
                    temp = min(temp, dp[remain])
            dp[i] = temp + 1
        if dp[amount] >= sys.maxsize:
            return -1
        return dp[amount]


print(Solution().coinChange([5], 5))
print(Solution().coinChange([1, 2, 5], 11))
print(Solution().coinChange([2], 3))
print(Solution().coinChange([1, 7, 11, 13, 17], 152))
print(Solution().coinChange(
    [70, 177, 394, 428, 427, 437, 176, 145, 83, 370], 7582))
print("--------------------")
