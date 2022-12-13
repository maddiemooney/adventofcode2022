def partone(lst):
    for i in range(3, len(lst)):
        buffer = [lst[i], lst[i-1], lst[i-2], lst[i-3]]
        if len(set(buffer)) == len(buffer):
            print(buffer)
            return i+1
    return -1

def parttwo(lst):
    buffers = [lst[i-14:i] for i in range(14, len(lst))]
    for j in range(0,len(buffers)):
        if len(set(buffers[j])) == len(buffers[j]):
            print(buffers[j])
            return j+14
    return -1



file1 = open('input.txt', 'r')
lst = file1.read()

print(partone(lst))
print(parttwo(lst))
