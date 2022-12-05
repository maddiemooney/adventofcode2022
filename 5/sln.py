
def partone(crates, instructions):
	final = ''
	for inst in instructions:
		for i in range(0, inst[0]):
			char = crates[inst[1]-1].pop()
			crates[inst[2]-1].append(char)
	for crate in crates:
		final+=(crate[-1])
	return final

def parttwo(crates, instructions):
	final = ''
	for inst in instructions:
		tmp = []
		for i in range(0, inst[0]):
			tmp.insert(0,crates[inst[1]-1].pop())
		for t in tmp:
			crates[inst[2]-1].append(t)
	for crate in crates:
		final+= crate[-1]
	return final


file1 = open('input.txt', 'r')

cratelines = []
instructions = []
crates = []
for line in file1.readlines():
	if "move" in line:
		instructions.append(list(map(int, line.split()[1::2])))
	elif '[' in line:
		cratelines.append(line)	
	elif len(line):
		line = line.strip()
		heehoo = list(map(int, line.split()))
		if len(heehoo):
			for i in range(0, max(heehoo)):
				crates.append([])

for line in cratelines:
	iter = 0
	for idx in range(1, len(line), 4):
		if line[idx] != ' ':
			crates[iter].insert(0, line[idx])
		iter += 1

#print(partone(crates, instructions))
print(parttwo(crates, instructions))


