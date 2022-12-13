from math import trunc
# not doing parsing on this one bud

def tm1(items, monkeys):
	if len(items) == 0:
		return 0
	for item in items:
		new_worry = item * 19
		new_worry = trunc(new_worry/3)
		if new_worry % 23 == 0:
			monkeys[2].append(new_worry)
		else:
			monkeys[3].append(new_worry)
	monkeys[0] = []
	return len(items)

def tm2(items, monkeys):
	if len(items) == 0:
		return 0
	for item in items:
		new_worry = item + 6
		new_worry = trunc(new_worry/3)
		if new_worry % 19 == 0:
			monkeys[2].append(new_worry)
		else:
			monkeys[0].append(new_worry)
	monkeys[1] = []
	return len(items)


def tm3(items, monkeys):
	if len(items) == 0:
		return 0
	for item in items:
		new_worry = item * item
		new_worry = trunc(new_worry/3)
		if new_worry % 13 == 0:
			monkeys[1].append(new_worry)
		else:
			monkeys[3].append(new_worry)
	monkeys[2] = []
	return len(items)

def tm4(items, monkeys):
	if len(items) == 0:
		return 0
	for item in items:
		new_worry = item + 3
		new_worry = trunc(new_worry/3)
		if new_worry % 17 == 0:
			monkeys[0].append(new_worry)
		else:
			monkeys[1].append(new_worry) 	
	monkeys[3] = [] 
	return len(items)
	
def m0(items, monkeys):
	for item in items:
		n = item * 7
		n = n % 9699690
		if n % 11 == 0:
			monkeys[2].append(n)
		else:
			monkeys[6].append(n)
	monkeys[0] = []
	return len(items)

def m1(items, monkeys):
	for item in items:
		n = item * 13
		n = n % 9699690
		if n % 5 == 0:
			monkeys[7].append(n)
		else:
			monkeys[4].append(n)
	monkeys[1] = []
	return len(items)

def m2(items, monkeys):
	for item in items:
		n = item + 1
		n = n % 9699690
		if n % 7 == 0:
			monkeys[1].append(n)
		else:
			monkeys[7].append(n)
	monkeys[2] = []
	return len(items)

def m3(items, monkeys):
	for item in items:
		n = item * item
		n = n % 9699690
		if n % 2 == 0:
			monkeys[0].append(n)
		else:
			monkeys[6].append(n)
	monkeys[3] = []
	return len(items)


def m4(items, monkeys):
	for item in items:
		n = item + 7
		n = n % 9699690
		if n % 17 == 0:
			monkeys[3].append(n)
		else:
			monkeys[5].append(n)
	monkeys[4] = []
	return len(items)

def m5(items, monkeys):
	for item in items:
		n = item + 6
		n = n % 9699690
		if n % 13 == 0:
			monkeys[3].append(n)
		else:
			monkeys[0].append(n)
	monkeys[5] = []
	return len(items)

def m6(items, monkeys):
	for item in items:
		n = item + 4
		n = n % 9699690
		if n % 3 == 0:
			monkeys[1].append(n)
		else:
			monkeys[2].append(n)
	monkeys[6] = []
	return len(items)

def m7(items, monkeys):
	for item in items:
		n = item + 8
		n = n % 9699690
		if n % 19 == 0:
			monkeys[4].append(n)
		else:
			monkeys[5].append(n)
	monkeys[7] = []
	return len(items)

def partone(test):
	#monkeys = []
	if test:
		monkeys = [[79,98], [54,65,75,74], [79,60,97], [74]]
		heehoo = [tm1, tm2, tm3, tm4]
	else:
		monkeys = [[54,82,90,88,86,54],[91,65],[62,54,57,92,83,63,63],[67,72,68], [68,89,90,86,84,57,72,84], [79,83,64,58], [96,72,89,70,88],[79]]

	totals = [0,0,0,0,0,0,0,0]
	for i in range(1,10001):
		#totals[0] += tm1(monkeys[0], monkeys)
		#totals[1] += tm2(monkeys[1], monkeys)
		#totals[2] += tm3(monkeys[2], monkeys)
		#totals[3] += tm4(monkeys[3], monkeys)
		#print(monkeys)

		totals[0] += m0(monkeys[0], monkeys)
		totals[1] += m1(monkeys[1], monkeys)
		totals[2] += m2(monkeys[2], monkeys)
		totals[3] += m3(monkeys[3], monkeys)
		totals[4] += m4(monkeys[4], monkeys)
		totals[5] += m5(monkeys[5], monkeys)
		totals[6] += m6(monkeys[6], monkeys)
		totals[7] += m7(monkeys[7], monkeys)
		
	totals.sort(reverse = True)
	print(totals)
	return totals[0] * totals[1]

print(partone(False))



