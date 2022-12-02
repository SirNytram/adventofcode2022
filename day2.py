handscores = {'A':1,'B':2,'C':3, 'X':1,'Y':2,'Z':3}
handequiv = {'A':'R','B':'P','C':'S', 'X':'R','Y':'P','Z':'S'}
battlescores = {'RR':3,'PP':3,'SS':3,'RP':6,'RS':0,'PR':0,'PS':6,'SR':6,'SP':0}
totscore = 0
lines = open('day2.txt').readlines()
for line in lines:
    line = line[:-1]
    battle = f'{handequiv[line[0]] + handequiv[line[2]]}'
    curscore = battlescores[battle]
    print(f'{line} - {curscore} - {handscores[line[2]]}')
    totscore = totscore + curscore + handscores[line[2]]
    
print(totscore)