"""
    1st attempt: hashtable + sort
    1 pass for iterating the words and put the words into corresponding hashtable
    1 pass for grouping the values from hashtable into the result
    Time O(n*klogk) n:number of words, k:length of charactors, klogk is due to the sorting
    Space O(nk)
    88 ms, faster than 99.89% 
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ht = {}
        for s in strs:
            sortedStr = self.sortString(s)
            if sortedStr in ht:
                ht[sortedStr].append(s)
            else:
                ht[sortedStr] = [s]
        res = []
        for key in ht:
            res.append(ht[key])
        return res

    def sortString(self, s):
        a = sorted(s)
        return "".join(a)


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print("-----")

"""
    2nd attempt: hashtable but base on charactor count
    although it doesnt sort(nlogn), it runs slower than the 1st due to the string manipulation
    Time O(nk) n:number of words, k:length of charactors
    Space O(nk)

    136 ms, faster than 46.18%
"""


class Solution(object):
    def groupAnagrams(self, strs):
        ht = {}
        for s in strs:
            encrypedtStr = self.encrypt(s)
            if encrypedtStr in ht:
                ht[encrypedtStr].append(s)
            else:
                ht[encrypedtStr] = [s]
        res = []
        for key in ht:
            res.append(ht[key])
        return res

    def encrypt(self, s):
        arr = 26*[0]
        for c in s:
            i = ord(c)-ord('a')
            arr[i] += 1
        alphbets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        key = ""
        # save the key as a0b1c1...z0
        for i in range(len(arr)):
            if arr[i] > 0:
                key += alphbets[i] + str(arr[i])
        return key


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print("-----")

"""
    3rd attempt: shorten the 2nd approach by just using string.join(list)

    Time O(nk) n:number of words, k:length of charactors
    Space O(nk)
    168 ms, faster than 18.21%
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ht = {}
        for s in strs:
            structure = 26*[0]
            for c in s:
                i = ord(c)-ord('a')
                structure[i] += 1
            key = ','.join([str(x) for x in structure])
            if key not in ht:
                ht[key] = [s]
            else:
                ht[key].append(s)
        res = []
        for key in ht:
            res.append(ht[key])
        return res
