str_ = input()
arr = str_.split(' ')
arr2 = []
for i in arr:
    length = len(i)
    arr2.append(f'{i} {length}')
print(arr2)