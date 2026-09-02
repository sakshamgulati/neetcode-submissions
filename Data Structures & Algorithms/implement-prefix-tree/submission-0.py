class Treenode:
    def __init__(self):
      self.hashmap={}
      self.word= False

class PrefixTree:

    def __init__(self):
        self.treenode= Treenode()
        

    def insert(self, word: str) -> None:
        head=self.treenode
        for w in word:
            if w not in head.hashmap:
                head.hashmap[w]= Treenode()
            head=  head.hashmap[w]
        head.word= True
        return None


    def search(self, word: str) -> bool:
        head= self.treenode
        for w in word:
          if w not in head.hashmap:
            return False
          else:
            head= head.hashmap[w]
        return head.word
        

    def startsWith(self, prefix: str) -> bool:
        head= self.treenode
        for w in prefix:
            if w not in head.hashmap:
                return False
            else:
                head=head.hashmap[w] #[s]->[a]
      
        return True
        
        