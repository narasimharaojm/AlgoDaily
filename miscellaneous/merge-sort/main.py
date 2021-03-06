class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        merge sort: https://www.geeksforgeeks.org/merge-sort/
        - divides input array into two halves recursively
        - merge two sorted halves and then return
        - this version occupies space(not in-place)
        - first divide, second process; the procedure is similar to post order traversal
        Time	O(nlogn)
        Space O(n)
        """
        self.quicksort(nums, 0, len(nums)-1)
        return nums

    def mergesort(self, nums):
        if len(nums) == 1:
            return nums
        half = len(nums)/2
        left = self.mergesort(nums[:half])
        right = self.mergesort(nums[half:])
        res = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        if i < len(left):
            res += left[i:]
        if j < len(right):
            res += right[j:]
        return res
