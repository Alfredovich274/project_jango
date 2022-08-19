a = [15, None, 'rur']
a.remove(None)
a = [str(i) for i in a]

# print(' '.join(a))
b = [1]
if None not in b:
    print('B Yes')
else:
    print('B No')
c = []
if (None not in b) or c:
    print('C Yes')
else:
    print('C No')
