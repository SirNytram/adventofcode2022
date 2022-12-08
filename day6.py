

def day6(line, numchars=4):
    
    for i in range(len(line)-numchars):
        marker = line[i:i+numchars]
        if len(set(marker)) == numchars:
            print(f'answer ({numchars}): {i + numchars}')
            break



lines = ['mjqjpqmgbljsphdztnvjfqwrcgsmlb','bvwbjplbgvbhsrlpgdmjqwftvncz','nppdvjthqldpwncqszvftbrmjlhg','nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg','zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 
            open('day6.txt').readlines()[0]]
for line in lines:
    day6(line)
    day6(line, 14)




