from collections import Counter
class Solution:
    """We check if deleting a letter from the string 
    will give us a set of frequencies of other letters 
    with len == 1, basically that every other letter
    occurs same number of times
    """
    # def equalFrequency(self, word: str) -> bool:
    #     for i, _ in enumerate(word):
    #         if len(set(Counter((word[:i]+word[i+1:])).values())) == 1:
    #             return True
            
    #     return False
    def equalFrequency(self, word: str) -> bool:
        for i, _ in enumerate(word):
        #   print(word[:i]+word[i+1:])  
          print(len(set(Counter((word[:i]+word[i+1:])).values())))

        
obj=Solution().equalFrequency('abcdc')
print(obj)