x = int(input())
for i in range(2, x+2):
	for j in range(i):
		print("", end="")
	for j in range(1, i):
		print(j, end="")
	print()