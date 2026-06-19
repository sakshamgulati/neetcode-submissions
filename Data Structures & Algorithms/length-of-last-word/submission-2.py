class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        fp,sp=0,0
        space=False
        while sp < len(s):
            if s[sp]==" ":
                fp=sp
                space= True
            else:
                if space:
                    last_word= sp-fp
                else:
                    last_word= sp-fp+1
            sp+=1
        return last_word
        