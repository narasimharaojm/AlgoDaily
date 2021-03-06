import heapq


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
    3rd approach: heap (its actually=sort)
	- iterate the list and put all the values into an array
	- sort the array
	- make that array into a linked list
    
	Time	O(NlogN) N=n*k
	Space	O(N)
	124 ms, faster than 41.48% 
"""


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq = []
        for l in lists:
            cur = l
            while cur != None:
                heapq.heappush(pq, cur.val)
                cur = cur.next
        dump = ListNode(0)
        cur = dump
        while len(pq) > 0:
            pop = heapq.heappop(pq)
            node = ListNode(pop)
            cur.next = node
            cur = cur.next
        return dump.next
