"""
    Find out the total number of 2 numbers that can sum up to a value which is less than or equal to the target

    Note:
    - will there be an empty array? yes
    - will there be a single item array? yes
    - all numbers are positive? yes
    - any duplicate? no

    e.g.1 [1,3,5,7,9], target=10

    return 6

    because
    [1,3]
    [1,5]
    [1,7]
    [1,9]
    [3,5]
    [3,7]

    e.g.2 [1,3,5,7,9], target=16

    return 10

    because
    [1,3]
    [1,5]
    [1,7]
    [1,9]
    [3,5]
    [3,7]
    [3,9]
    [5,7]
    [5,9]
    [7,9]
"""


"""
    Time    O(nlogn)
    Space   O(1)
"""


def twoSumCombo(nums, target):
    nums = sorted(nums)
    res = 0
    for i in range(len(nums)):
        num = nums[i]
        idx = bsearch(nums, target-num)
        if idx > -1 and idx > i:
            res += idx - i
    return res


def bsearch(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right)/2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid
    # to find number that no larger than target
    return right


a = [1, 3, 5, 7, 9]
print(twoSumCombo(a, 10))
print(twoSumCombo(a, 16))
print(twoSumCombo(a, 1))

a = [1]
print(twoSumCombo(a, 10))


"""
    follow-up: what if we want to find out all combinations?

    Time    O(2^n)
    Space   O(2^n)
"""


class Solution(object):

    def __init__(self):
        self.res = 0

    def allCombo(self, nums, target):
        self.dfs(nums, target, 0)
        return self.res

    def dfs(self, nums, target, total):
        if total <= target:
            self.res += 1
        if total < target:
            for i in range(len(nums)):
                self.dfs(nums[i+1:], target, total+nums[i])


a = [1, 3, 5, 7, 9]
print(Solution().allCombo(a, 10))
