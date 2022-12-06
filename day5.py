isTesting = True
import os
file = os.path.basename(__file__)[:-3]
if isTesting:
    file += 'ex'
lines = open(file + '.txt').readlines()

def debug(text):
    if isTesting:
        print(text)

for line in lines:
    debug(line[:-1])
