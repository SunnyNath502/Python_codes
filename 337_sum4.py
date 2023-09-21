nums = [1,2,3]
target = 4
s=sorted(nums,reverse=True)
count=0
for i in range (len(s)-1):
    for j in range(len(s)-2):
        