from pygame import Vector2 as V  
def isnear(head, tail):
	return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1
	
def isdiag(head, tail, direc):
	if direc == 'U' or direc == 'D':
		return abs(head[0] - tail[0]) == 1
	elif direc == 'L' or direc == 'R':
		return abs(head[1] - tail[1]) == 1

def partone(lst):

	head = [0,0]
	tail = [0,0]

	visited = set()

	for cmd in lst:
		#print(cmd)
		direc = cmd[0]
		dist = int(cmd[1])
		
		if direc == 'U':
			for i in range(dist):
				head[1] += 1
				if not isnear(head, tail):
					if isdiag(head, tail, direc):
						tail[0] = head[0]
					tail[1] += 1
				visited.add(str(tail[0])+str(tail[1]))
		elif direc == 'D':
			for i in range(dist):
				head[1] -= 1
				if not isnear(head, tail):
					if isdiag(head, tail, direc):
						tail[0] = head[0]
					tail[1] -= 1
				visited.add(str(tail[0])+str(tail[1]))
		elif direc == 'L':
			for i in range(dist):
				head[0] -= 1
				if not isnear(head, tail):
					if isdiag(head, tail, direc):
						tail[1] = head[1]
					tail[0] -= 1
				visited.add(str(tail[0])+str(tail[1]))
		elif direc == 'R':	
			for i in range(dist):
				head[0] += 1	
				if not isnear(head, tail):
					if isdiag(head, tail, direc):
						tail[1] = head[1]
					tail[0] += 1
				visited.add(str(tail[0])+str(tail[1]))
		#print(head, tail)
	#print(visited)
	return len(visited)

def move(rope):
  for i in range(len(rope)-1):
    s1, s2 = rope[i], rope[i+1]
    if s1.distance_to(s2) >= 2:
      dx, dy = s1 - s2
      if abs(dx) > 1:  dx //= abs(dx)
      if abs(dy) > 1:  dy //= abs(dy)
      rope[i+1] = s2 + V(dx, dy)
  return rope    


def solve(puzzle, rope_length):
  DIR = dict(R=V(1, 0), L=V(-1, 0), U=V(0, -1), D=V(0, 1))
  rope, tail_trail = [V(0, 0)]*rope_length, set()
  for dir, steps in puzzle:
    for _ in range(int(steps)):
      rope[0] = rope[0] + DIR[dir]
      rope = move(rope)
      tail_trail.add(tuple(rope[-1]))
  return len(tail_trail) 

file1 = open('input.txt', 'r')
lst = [line.strip().split() for line in file1.readlines()]

print(solve(lst,2))
print(solve(lst,10))

