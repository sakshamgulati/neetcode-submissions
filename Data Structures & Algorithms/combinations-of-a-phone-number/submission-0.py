class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans,subset=[],[]
        mapping={
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"],
        }
        if len(digits)==0:return ans
        def dfs(i):
            if i > len(digits):
                return
            if i == len(digits):
                ans.append(''.join(c for c in subset.copy()))
                return
            for chars in mapping[digits[i]]:
                subset.append(chars)
                dfs(i+1)
                subset.pop()

        dfs(0)
        return ans
