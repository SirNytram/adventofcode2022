handscores = {'A':1,'B':2,'C':3, 'X':1,'Y':2,'Z':3}
handequiv = {'A':'R','B':'P','C':'S', 'X':'R','Y':'P','Z':'S'}
battlescores = {'RR':3,'PP':3,'SS':3,'RP':6,'RS':0,'PR':0,'PS':6,'SR':6,'SP':0}
neededhands = {'A X':'Z','A Y':'X','A Z':'Y',
               'B X':'X','B Y':'Y','B Z':'Z',
               'C X':'Y','C Y':'Z','C Z':'X'}

totscore = 0
lines = open('day2.txt').readlines()
for line in lines:
    line = line[:-1]
    neededhand = neededhands[line]
    # battle = f'{handequiv[line[0]] + handequiv[line[2]]}'
    battle = f'{handequiv[line[0]] + handequiv[neededhand]}'
    curscore = battlescores[battle]
    
    # curhs = handscores[line[2]]
    curhs = handscores[neededhand]
    print(f'{line} - {battle} - {curscore} - {curhs}')
    totscore = totscore + curscore + curhs
    
print(totscore)



