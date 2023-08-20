

s = 'abcdaba'
res=0
r=[]
uniq=set(s)
for c in uniq:
    left = s.find(c)
    right=s.rfind(c)
    if left<right:
       res+=len([(s[left+1:right])])
print(res)
# print(left)
# print(right)

            
        


