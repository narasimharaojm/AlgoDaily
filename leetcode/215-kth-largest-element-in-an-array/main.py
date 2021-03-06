"""
    2nd approach: upper bound binary search

    Time    O(n * (logk + k)) since insert takes O(k)
    Space   O(k)
    112 ms, faster than 33.23% 
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0 or k <= 0:
            return -1
        window = []
        for num in nums:
            idx = self.upperbsearch(window, num)
            window.insert(idx, num)
            if len(window) > k:
                window.pop(0)
        return window[0]

    def upperbsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left


"""
    2nd approach
	- max heap

	Time		O(nlogn + klogk)
	Space		O(n)
	84 ms, faster than 44.00%
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0 or k <= 0:
            return -1
        pq = []
        for num in nums:
            heapq.heappush(pq, (-num))
        i = 0
        res = -1
        while len(pq) > 0 and i < k:
            res = -heapq.heappop(pq)
            i += 1
        return res
