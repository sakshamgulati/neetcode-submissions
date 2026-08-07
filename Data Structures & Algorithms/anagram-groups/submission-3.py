class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import defaultdict
        hm= defaultdict(list)
        ans=[]
        for word in strs:
            sorted_word= tuple(sorted(word))
            if sorted_word not in hm.keys():
                hm[sorted_word]=[word]
            else:
                hm[sorted_word].append(word)
        for key,vals in hm.items():
            ans.append(vals)
        return ans