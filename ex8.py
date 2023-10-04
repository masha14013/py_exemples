for i in range(2, 11):
	for j in range(10 - i):
		print(" ", end="")
	for j in range(1, i):
		print(j, end="")
	print()
for i in range(9, 0, -1):
	for j in range(9):
		print(" ", end="")
	for j in range(i, 0, -1):
		print(j, end="")
	print()

"""for i in range(2, 11):
	for j in range(11):
		print(" ", end="")
	for j in range(1, i):
		print(j, end="")
	print()"""
