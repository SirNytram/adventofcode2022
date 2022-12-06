isTesting = False
import os
file = os.path.basename(__file__)[:-3]
if isTesting:
    file += 'ex'
lines = open(file + '.txt').readlines()

def debug(text):
    # if isTesting:
        print(text)

totinside = toteq = 0
for line in lines:
    line = line[:-1]
    pairs = line.split(',')
    minmaxs0 = pairs[0].split('-')
    minmaxs1 = pairs[1].split('-')
    min1 = int(minmaxs0[0])
    max1 = int(minmaxs0[1])
    min2 = int(minmaxs1[0])
    max2 = int(minmaxs1[1])

    # charpos = line.find('-')
    # min1 = line[0:charpos]
    # max1 = line[charpos+1:line.find(',')]

    # line2 = line[line.find(',')+1:] 
    # charpos = line2.find('-')
    # min2 = line2[0:charpos]
    # max2 = line2[charpos+1:]
    # debug(f'{line} 1:{min1}-{max1} 2:{min2}-{max2}')

    first = False
    if (min1 == min2 and max1 == max2):
        debug(f'{line} 1:{min1}-{max1} 2:{min2}-{max2}')
        debug('eq')
        toteq += 1
    else:

        if (min2 <= min1) and (max2 >= max1):
            totinside += 1
            # debug(f'{line} 1:{min1}-{max1} 2:{min2}-{max2}')
            # debug('1st pair is inside')
            first = True

        
        if (min1 <= min2) and (max1 >= max2):
            totinside += 1
            # if first:
            # debug(f'{line} 1:{min1}-{max1} 2:{min2}-{max2}')
            # debug('2nd pair is inside')





print(f'total: {totinside}')
print(f'total eq: {toteq}')
print(f'total: {totinside + toteq}')
