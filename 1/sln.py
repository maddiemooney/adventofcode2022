def partone(lst):
	elfs = []
	elftotal = 0
	for elf in lst:
		if elf == '':
			elfs.append(elftotal)
			elftotal = 0
		else:
			elftotal += int(elf)
	
	return max(elfs)

def parttwo(lst):
	elfs = []
	elftotal = 0
	for elf in lst:
		if elf == '':
			elfs.append(elftotal)
			elftotal = 0
		else:
			elftotal += int(elf)
	elfs.sort(reverse=True)
	return (elfs[0] + elfs[1] + elfs[2])


file1 = open('input.txt', 'r')
lst = [line.strip() for line in file1.readlines()]

print(partone(lst))
print(parttwo(lst))
