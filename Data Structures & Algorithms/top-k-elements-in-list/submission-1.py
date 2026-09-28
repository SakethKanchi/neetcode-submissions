class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            res[num] = 1 + res.get(num,0)
        
        freq = [[] for i in range(len(nums) + 1)]

        for key,v in res.items():
            freq[v].append(key)
        
        ans = []
        for i in range(len(freq)-1,-1,-1):
            for  num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans