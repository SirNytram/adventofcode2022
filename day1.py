elves = []
totqty = 0
maxqty = 0
maxelve = 0
f = open('day1.txt')
lines = f.readlines()
for line in lines:
    if line == '\n':
        # print(f'empty {line}')
        elves.append(totqty)
        totqty = 0
    else:
        curqty = int(line[:-1])
        totqty += curqty
        # print('not empty')


elves.append(totqty)
print(totqty)
if maxqty < totqty:
    maxqty = totqty

elves.sort(reverse=True)

print(elves)
print(f'top 3: {elves[0] + elves[1] + elves[2]}')