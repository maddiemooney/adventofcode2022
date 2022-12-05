import itertools

values = {
	"a": 1,
	"b": 2,
	"c": 3, 
	"d": 4,
	"e": 5,
	"f": 6,
	"g": 7,
	"h": 8 ,
	"i": 9,
	"j": 10,
	"k": 11,
	"l":12,
	"m":13,
	"n":14,
	"o":15,
	"p":16,
	"q":17,
	"r":18,
	"s":19,
	"t":20,
	"u":21,
	"v":22,
	"w":23,
	"x":24,
	"y":25,
	"z":26,
	"A":27,
	"B":28,
	"C":29,
	"D":30,
	"E":31,
	"F":32,
	"G":33,
	"H":34,
	"I":35,
	"J":36,
	"K":37,
	"L":38,
	"M":39,
	"N":40,
	"O":41,
	"P":42,
	"Q":43,
	"R":44,
	"S":45,
	"T":46,
	"U":47,
	"V":48,
	"W":49,
	"X":50,
	"Y":51,
	"Z":52
} 
def repeat(object, times=None):
    # repeat(10, 3) --> 10 10 10
    if times is None:
        while True:
            yield object
    else:
        for i in range(times):
            yield object

def zip_longest(*args, fillvalue=None):
    # zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
    iterators = [iter(it) for it in args]
    num_active = len(iterators)
    if not num_active:
        return
    while True:
        values = []
        for i, it in enumerate(iterators):
            try:
                value = next(it)
            except StopIteration:
                num_active -= 1
                if not num_active:
                    return
                iterators[i] = repeat(fillvalue)
                value = fillvalue
            values.append(value)
        yield tuple(values)

def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == 'fill':
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == 'strict':
        return zip(*args, strict=True)
    if incomplete == 'ignore':
        return zip(*args)
    else:
        raise ValueError('Expected fill, strict, or ignore')

def partone(lst):
	
	total = 0
	for sack in lst:
		first = set(sack[:int(len(sack)/2)])
		second = set(sack[int(len(sack)/2):])
		total += values[first.intersection(second).pop()]
	return total

def parttwo(lst):
	total = 0
	groups = list(grouper(lst,3))
	for g in groups:
		first = set(g[0])
		second = set(g[1])
		third = set(g[2])
		total += values[first.intersection(second).intersection(third).pop()]
	return total

file1 = open('input.txt', 'r')
lst = [line.strip() for line in file1.readlines()]

print(partone(lst))
print(parttwo(lst))

