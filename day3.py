import os
file = os.path.basename(__file__)[:-3]
isTesting = False
if isTesting:
    file += 'ex'
lines = open(file + '.txt').readlines()


def lettertoval(letter):
    val = 0
    lettervalue = ord(letter)
    if lettervalue < 97:
        val = lettervalue - 38
    else:
        val = lettervalue  - 96
    return val
backpacks= []
totvalue = 0



for line in lines:
    line = line[:-1]
    part1 = line[0:int(len(line)/2)]
    part2 = line[int(len(line)/2):]
    if isTesting:
        print(part1)
        print(part2)
    isFound = False
    for letter in part1:
        if part2.find(letter) != -1:
            isFound = True
            lettervalue = lettertoval(letter)
            totvalue += lettervalue
            if isTesting:
                print(f'letter: {letter} value: {lettervalue}')
            backpacks.append([line, part1, part2, letter, lettervalue])
            break
print(f'total: {totvalue}')


totvalue = 0
line1 = ''
line2 = ''
line3 = ''
for no, line in enumerate(lines):
    endofgroup  = False
    if (no + 1) % 3 == 0:
        line3 = line

        endofgroup = True
        
    elif (no + 1) % 2 == 0:
        line2 = line
    else:
        line1 = line
        
    if endofgroup:
        linetouse = ''
        # if len(line1) < len(line2):
        #     if len(line1) < len(line3):
        #         linetouse = line1
        #     else:
        #         linetouse = line3
        # else:
        #     if len(line2) < len(line3):
        #         linetouse = line2
        #     else:
        #         linetouse = line3
        for letter in line1:
            if line2.find(letter) != -1 and line3.find(letter) != -1:
                lettervalue = lettertoval(letter)
                totvalue += lettervalue
                if isTesting:
                    print(f'letter: {letter} value: {lettervalue}')
                break

print(f'total: {totvalue}')
