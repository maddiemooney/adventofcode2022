
def partone(lst):
	reg = 1
	cycle = 0
	pause = [20,60,100,140,180,220]
	total = 0
	for cmd in lst:
		if cmd[0] == "noop":
			cycle += 1
			if cycle in pause:
				total += cycle * reg
		elif cmd[0] == "addx":
			cycle += 1
			if cycle in pause:
				total += cycle * reg
			cycle += 1
			if cycle in pause:
				total += cycle * reg
			reg += int(cmd[1])
	return total

def draw(pos, reg):
	if reg == pos-1 or reg == pos or reg == pos +1:
		return '#'
	else:
		return '.'

def parttwo(lst):
	reg = 1
	cycle = 0
	row = ''
	pos = 0
	
	for cmd in lst:
		
		if cmd[0] == "noop":
			cycle += 1
			if pos == 40:
				print(row)
				row = ''
				pos = 0
			else:
				row += draw(pos, reg)
				pos += 1
		elif cmd[0] == "addx":
			cycle += 1
			if pos == 40:
				print(row)
				row = ''
				pos = 0
			else:
				row += draw(pos, reg)
				pos += 1
			
			cycle += 1
			if pos == 40:
				print(row)
				row = ''
				pos = 0
			else:
				row += draw(pos, reg)
				pos += 1
			reg += int(cmd[1])
			
	print(row)
	return 0

file1 = open('input.txt', 'r')
lst = [line.strip().split() for line in file1.readlines()]

print(partone(lst))
print(parttwo(lst))

