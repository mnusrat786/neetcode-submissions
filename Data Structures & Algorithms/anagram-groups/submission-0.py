class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            b = "".join(sorted(i))
            res[b].append(i) 
        return list(res.values())    


        
        