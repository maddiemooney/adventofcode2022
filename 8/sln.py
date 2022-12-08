def leftneighbors(coord, trees):
    x = coord[0]
    y = coord[1]
    return trees[y][0:x]

def rightneighbors(coord, trees):
    x = coord[0]
    y = coord[1]
    return trees[y][x+1:len(trees[y])]

def upneighbors(coord, trees):
    x = coord[0]
    y = coord[1]
    n = []
    for i in range(0, y):
        n.append(trees[i][x])
    return n

def downneighbors(coord, trees):
    x = coord[0]
    y = coord[1]
    n = []
    for i in range(y+1, len(trees)):
        n.append(trees[i][x])
    return n

def partone(lst):
    alltrees = len(lst) * len(lst[0])
    totalhidden = 0

    for i in range(1, len(lst)-1):
        for j in range(1, len(lst[0])-1):
            coord = (j,i)
            #print("\n- "+str(coord[0])+','+str(coord[1]))
            val = lst[i][j]
            l = leftneighbors(coord, lst)
            r = rightneighbors(coord, lst)
            u = upneighbors(coord, lst)
            d = downneighbors(coord, lst)
            #print(l, r, u, d)
            if val <= max(l) and val <= max(r) and val <= max(u) and val <= max(d):
                #print(str(val)+"^ hidden")
                totalhidden += 1


    return alltrees - totalhidden

def finddistance(val, neighbors):
    for i in range(0, len(neighbors)):
        if val <= neighbors[i]:
            return i+1
    return len(neighbors)

def parttwo(lst):
    bestscore = 0
    for i in range(1,len(lst)-1):
        for j in range(1, len(lst[0])-1):
            coord = (j,i)
            val = lst[i][j]
            l = leftneighbors(coord, lst)
            r = rightneighbors(coord,lst)
            u = upneighbors(coord,lst)
            d = downneighbors(coord,lst)

            #print(coord,val)
            ls = finddistance(val, l[::-1])
            rs = finddistance(val, r)
            us = finddistance(val, u[::-1])
            ds = finddistance(val, d)
            #print(ls, rs, us, ds, '\n')

            score = ls * rs * us * ds
            if score > bestscore:
                bestscore = score

    return bestscore


file1 = open('input.txt', 'r')
lst = [[int(x) for x in line.strip()] for line in file1.readlines()]

print(partone(lst))
print(parttwo(lst))