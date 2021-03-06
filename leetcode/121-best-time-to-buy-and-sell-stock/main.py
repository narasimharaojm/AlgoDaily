import heapq

"""
    1st approach: classic dp problem
    - keep the bay when we traverse the list
    - when there is a new peak and the current diff is larger than the previous diff, update the diff

    Time    O(n)
    Space   O(1)
    20 ms, faster than 100.00%
"""
class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        bay = prices[0]
        diff = 0
        for price in prices:
            if price < bay:
                bay = price
            if price - bay > diff:
                diff = price - bay
        return diff


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
print(Solution().maxProfit([2, 4]))
print(Solution().maxProfit([2, 4, 1]))
print(Solution().maxProfit([2, 4, 1, 4]))

print("-----")

"""
    optimize 1st approach: classic dp problem
    - keep the bay when we traverse the list
    - when there is a new peak and the current diff is larger than the previous diff, update the diff

    Time    O(n)
    Space   O(1)
    52 ms, faster than 48.09%
"""
class Solution(object):
    def maxProfit(self, prices):
        res = 0
        dip = sys.maxsize
        for price in prices:
            dip = min(dip, price)
            res = max(res, price-dip)
        return res

print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
print(Solution().maxProfit([2, 4]))
print(Solution().maxProfit([2, 4, 1]))
print(Solution().maxProfit([2, 4, 1, 4]))

print("-----")

"""
    2nd approach: priority queue
    - keep pushing the number into the priority
    - in each iteration, if each price - min(priority queue) is larger than the result, update the result

    Time    O(nlogn)
    Space   O(n) heap
    44 ms, faster than 16.01%
"""
class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        pq = []
        diff = 0
        for price in prices:
            heapq.heappush(pq, price)
            if price - pq[0] > diff:
                diff = price - pq[0]
        return diff


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
print(Solution().maxProfit([2, 4]))
print(Solution().maxProfit([2, 4, 1]))
print(Solution().maxProfit([2, 4, 1, 4]))
