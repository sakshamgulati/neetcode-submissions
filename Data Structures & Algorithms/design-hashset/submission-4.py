class MyHashSet:

    def __init__(self):
        self.hashlen = 5
        # This creates 5 distinct inner lists in memory
        self.hashlist = [[] for _ in range(self.hashlen)] 
    
    def hashfunction(self, key):
        return key % self.hashlen


    def add(self, key: int) -> None:
        _index = self.hashfunction(key)
        # Bonus bug fix: Check for duplicates so it behaves like a true Set!
        if key not in self.hashlist[_index]:
            self.hashlist[_index].append(key)

    def remove(self, key: int) -> None:
        _index = self.hashfunction(key)
        # Simplified removal logic
        if key in self.hashlist[_index]:
            self.hashlist[_index].remove(key)

    def contains(self, key: int) -> bool:
        _index = self.hashfunction(key)
        return key in self.hashlist[_index]