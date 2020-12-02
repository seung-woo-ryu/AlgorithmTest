class Node:
    def __init__(self):
        self.sons = dict()
        self.end = False
    
class Trie:

    def __init__(self):
        self.trie = Node()
    
    def insert(self, word: str) -> None:
        searchTrie = self.trie
        for w in word:
            if w not in searchTrie.sons:
                searchTrie.sons[w] = Node()
            searchTrie = searchTrie.sons[w]
        searchTrie.end = True
                    
    def search(self, word: str) -> bool:
        searchTrie = self.trie
        
        for w in word:
            if w not in searchTrie.sons:
                return False
            searchTrie = searchTrie.sons[w]
        if searchTrie.end:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        searchTrie = self.trie
        
        for w in prefix:
            if w not in searchTrie.sons:
                return False
            searchTrie = searchTrie.sons[w]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)