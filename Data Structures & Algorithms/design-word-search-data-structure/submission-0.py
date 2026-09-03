class TreeNode:
    def __init__(self):
        self.hashstore = {}
        self.word= False


class WordDictionary:

    def __init__(self):
        self.head = TreeNode()
        
        

    def addWord(self, word: str) -> None:
        curr = self.head
        for w in word:
            if w not in curr.hashstore:
                curr.hashstore[w]= TreeNode()
            curr = curr.hashstore[w]
        curr.word= True


    def search(self, word: str) -> bool:
        curr = self.head
        def dfs(curr,i):
            if i == len(word):
                return curr.word
            w = word[i]
            if w == ".":
                for children in curr.hashstore.values():
                    if dfs(children,i+1):
                        return True
                return False
            elif w not in curr.hashstore.keys():
                return False
            curr= curr.hashstore[w]
            return dfs(curr,i+1)
        return dfs(curr,0)
            
        
