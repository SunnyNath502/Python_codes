l = [[2, 1], [4, 2], [7, 8], [9, 10], [10, 11], [11, 12]]
p = sorted(l, key=lambda x: x[0])  # Sort by starting value of each pair
count = 1
end = p[0][1]

for i in range(1, len(p)):
    if end < p[i][0]:
        count += 1
        end = p[i][1]
    else:
        end = min(end, p[i][1])  # Adjust the ending value

print(count)
