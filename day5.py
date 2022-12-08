

isTesting = False
import os
file = os.path.basename(__file__)[:-3]
if isTesting:
    file += 'ex'
lines = open(file + '.txt').readlines()

def debug(text):
    if isTesting:
        print(text)

stacks = [[] for i in range(9)]
for line in lines:
    debug(line[:-1])

    if line.find('[') != -1:
        for i in range(9):

            pos = (4 * i)+1
            if pos < len(line):
                
                crate = line[pos]
                if crate != ' ':
                    stacks[i].insert(0, crate)
    elif line.find('move') != -1:
        words = line.split(' ')
        actQty = int(words[1])
        actFrom = int(words[3]) - 1
        actTo = int(words[5]) - 1
        debug(f'qty:{actQty} f:{actFrom} t:{actTo}')

        for i in range(actQty):
            stacks[actTo].append(stacks[actFrom].pop())
            debug(stacks)
            

debug(stacks)
answer = ''
for stack in stacks:
    if len(stack) > 0:
        answer += stack[-1]
print(f'answer: {answer}')



