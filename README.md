# Genetic-Algorithm
map=[[0,1,1,1,1,1,5],[0,0,0,0,0,1,1]]
for y in range(len(map)-1,-1,-1):
    for x in range(len(map[y])):
        print(map[y][x],end='|')
    print('\n')
a=0
b=0
#Các bước di chuyển
move=['r','r','r','r','r','u','r','d']
for i in move: 
    if i == 'u': b+=1
    if i == 'd': b-=1
    if i == 'r': a+=1
    if i == 'l': a-=1
    if map[b][a] == 0: continue
    if map[b][a] == 1: map[b][a] -= 1
    if map[b][a] == 2: map[b][a] -= 1
    if map[b][a] == 5: 
        for y in range(len(map)):
            for x in range(len(map[y])):
                if (map[y][x] !=0 ) and (map[y][x] != 5): continue
                else: 
                    print('Win')
                    break
for y in range(len(map)-1,-1,-1):
    for x in range(len(map[y])):
        print(map[y][x],end='|')
    print('\n')
