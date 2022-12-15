rawmap = open('day8.txt').read().split('\n')
# rawmap = ['30373', '25512', '65332', '33549', '35390']

# map = [[letter for letter in i] for i in rawmap]
print(rawmap)

numvisible = 0
for i,currow in enumerate(rawmap):
  for j,curheight in enumerate(currow):
    curheight = int(curheight)
    if i == 0 or i == len(rawmap)-1:
      #first and last rows
      numvisible += 1
    
    else:
      #middle rows
      if j == 0 or j == len(currow)-1:
        #first and last cols
        numvisible += 1
      else:
        # middle stuff, check all other sides(left,right,top,down) until we are longer
        #left
        seen = True
        # from postition to left edge
        for k in range(j-1,-1,-1):
          #if a tree is bigger, we're not seen anymore on this side
          if int(rawmap[i][k]) >= curheight:
            seen = False
            break

        if seen:
              numvisible += 1
        # if we're still seen, look right
        else:
          seen = True
          for k in range(j+1,len(currow)):
            if int(rawmap[i][k]) >= curheight:
              seen = False
              break

          # if we're still seen, look up
          if seen:
            numvisible +=1
          else:
            seen = True
            for k in range(i-1,-1, -1):
              if int(rawmap[k][j]) >= curheight:
                seen = False
                break

            if seen:
                numvisible += 1
            else:
              seen = True
              for k in range(i+1,len(rawmap)):
                if int(rawmap[k][j]) >= curheight:
                  seen = False
                  break

              if seen:
                numvisible += 1

print(f'numvisible: {numvisible}')