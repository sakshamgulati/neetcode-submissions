class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create an empty dictionary
        def init_dict():
            mydict={}
            for items in range(ord('a'),ord('a')+26+1):
                if items not in mydict:
                    mydict[items]=0
            return mydict
        
        map_s= init_dict()
        for char in s:
            map_s[ord(char)] +=1
        
        map_t = init_dict()
        for char in t:
            map_t[ord(char)] +=1
        
        return map_s==map_t


        
