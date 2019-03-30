a = list()

for _ in range(6):
    a.append(list(map(int, input().split())))
    
res = -(7*9)

for x in range(4):
    for y in range(4):
        hg = a[0+y][0+x] + \
             a[0+y][1+x] + \
             a[0+y][2+x] + \
             a[1+y][1+x] + \
             a[2+y][0+x] + \
             a[2+y][1+x] + \
             a[2+y][2+x]
        res = max(res, hg)
print(res)