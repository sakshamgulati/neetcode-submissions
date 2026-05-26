class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        sorted_dict= defaultdict(list)
        ans=[]
        for items in strs:
            key = tuple(sorted(items))
            if key in sorted_dict:
                sorted_dict[key].append(items)
            else:
                sorted_dict[key]=[items]
        for key,value in sorted_dict.items():
            ans.append(value)
        return ans