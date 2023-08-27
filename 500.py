class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a="qwertyuiop"
        b="asdfghjkl"
        c="zxcvbnm"
        ans=[]
        for i in words:
            # //i being each string in the list
            # // making i lower and assigning row to x
            y=i[0].lower()
            if y in a:
                x=a
            elif y in b:
                x=b
            else:
                x=c
            for j in i.lower():
            # //if not in same row then breaks 
                if j not in x:
                    break
        # //if loop is successful enters else part and appends the i to ans
            else:ans.append(i)
        return ans