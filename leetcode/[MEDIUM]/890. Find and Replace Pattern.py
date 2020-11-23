class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        if len(pattern) == 1:
            return words
        
        answer = list()
        
        for word in words:
            flag = True
            wordDict = dict()
            patternDict = dict()
            
            for idx, w in enumerate(word):
                if w not in wordDict:
                    wordDict[w] = pattern[idx]
                    if pattern[idx] not in patternDict:
                        patternDict[pattern[idx]] = w
                    else:
                        if patternDict[pattern[idx]] != w:
                            flag = False
                            break
                else:
                    if wordDict[w] != pattern[idx]:
                        flag = False
                        break
            if flag:
                answer.append(word)
        return answer