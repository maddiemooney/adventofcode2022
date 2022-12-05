
def partone(lst):
	total = 0
	total2 = 0
	for group in lst:
		pair = group.split(',')
		first = pair[0].split('-')
		second = pair[1].split('-')
		firstset = set()
		secondset = set()
		for i in range(int(first[0]),int(first[1])+1):
			firstset.add(i)
		for j in range(int(second[0]), int(second[1])+1):
			secondset.add(j)
		if firstset.issubset(secondset) or secondset.issubset(firstset):
			total += 1
		if len(secondset.intersection(firstset)) != 0:
			total2 += 1
	return (total, total2)



file1 = open('input.txt', 'r')
lst = [line.strip() for line in file1.readlines()]

print(partone(lst))

