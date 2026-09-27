class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            res[num] = 1 + res.get(num,0)
        
        a = []
        for key,value in res.items():
            a.append((value,key))
        
        a = sorted(a,reverse =True)
        top = a[:k]
        ans = []
        for num,count in top:
            ans.append(count)
        return ans