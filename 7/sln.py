from collections import defaultdict

def makedirs(lst):
    path, dirs = [], defaultdict(int)
    for cmd in lst:
        tokens = cmd.split()
        if tokens[0] == '$':
            if tokens[1] == "cd":
                if tokens[2] == "..":
                    path.pop()
                elif tokens[2] == '/':
                    path = ['/']
                else:
                    path.append(tokens[2])
        elif tokens[0] != "dir":
            for i in range(0, len(path)):
                dirs[tuple(path[:i+1])] += int(tokens[0])
    return dirs

def partone(lst):
    dirs = makedirs(lst)
    return (sum(total for total in dirs.values() if total <= 100000))

def parttwo(lst):
    dirs = makedirs(lst)
    needed = 30000000 - (70000000 - dirs[('/',)])
    return min(total for total in dirs.values() if total >= needed)

file1 = open('input.txt', 'r')
lst = [line.strip() for line in file1.readlines()]

print(partone(lst))
print(parttwo(lst))