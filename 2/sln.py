# A,X - rock     = 1
# B,Y - paper    = 2
# C,Z - scissors = 3

# A > Z
# B > X
# C > Y

# X > C
# Y > A
# Z > B

# win = 6
# draw = 3
# lose = 0

rock = ['A', 'X']
paper = ['B', 'Y']
scissors = ['C', 'Z']

def partone(lst):
	total = 0
	for game in lst:
		# draw
		if ord(game[1]) - ord(game[0]) == 23:
			total += 3
		# win
		elif ord(game[1]) - ord(game[0]) == 24 or ord(game[1]) - ord(game[0]) == 21:
			total += 6
		else:
			pass
		total += ord(game[1]) - 87
	return total

# X lose
# Y draw
# Z win

def parttwo(lst):
	total = 0
	for game in lst:
		# draw
		if game[1] == 'Y':
			total += 3
			total += ord(game[0]) - 64
		elif game[1] == 'Z':
			total += 6
			if game[0] == 'C':
				total += 1
			else:
				total += ord(game[0]) - 63
		elif game[1] == 'X':
			if game[0] == 'A':
				total += 3
			else:	
				total += ord(game[0]) - 65
	return total			


file1 = open('input.txt', 'r')
lst = [line.strip().split() for line in file1.readlines()]

print(partone(lst))
print(parttwo(lst))
