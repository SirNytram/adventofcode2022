

def day6(line):
    for i in range(len(line)-4):
        marker = line[i:i+4]
        if len(set(marker)) == 4:
            print(f'answer: {i + 4}')
            break



lines = ['mjqjpqmgbljsphdztnvjfqwrcgsmlb','bvwbjplbgvbhsrlpgdmjqwftvncz','nppdvjthqldpwncqszvftbrmjlhg','nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg','zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 
            open('day6.txt').readlines()[0]]
for line in lines:
    day6(line)




