class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        substack=[]

        def dfs(open_len,close_len):

            #base case
            if len(substack.copy()) == 2*n:
                ans.append(''.join(substack.copy()))
                return 
            
            #choices
            # 1- to add open parenthesis if len ("(") > n
            if open_len < n:
                substack.append("(")
                dfs(open_len+1, close_len)
                substack.pop()
                
            

            # choice 2- add closing bracket when len (")") > len closing string
            if open_len > close_len:
                substack.append(")")
                dfs(open_len, close_len +1)
                substack.pop()
        dfs(0,0)
        return ans
