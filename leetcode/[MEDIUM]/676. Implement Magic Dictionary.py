class MagicDictionary:

    def __init__(self):
        self.di = dict()
        

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            if len(word) not in self.di:
                self.di[len(word)] = [word]
            else:
                self.di[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        if len(searchWord) in self.di:
            for w in self.di[len(searchWord)]:
                temp = 0
                for a,b in zip(w,searchWord):
                    if a != b:
                        temp += 1
                if temp == 1:
                    return True
            return False
                    
        
        else:
            return False
            
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)