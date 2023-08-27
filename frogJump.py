stones = [0,1,3,5,6,8,12,17]
n=len(stones)
dp={}
for stone in stones:
    dp[stone]=set()
dp[0].add(0)  # Start from the first stone with jump size 0


for jump in dp[stones[]]:
    print(jump)