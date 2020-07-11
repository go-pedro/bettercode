names=['Corey','Chris','Dave','Travis']

#standard
# index=0
# for name in names:
# 	print (index, name)
# 	index+=1

#better code
for index, name in enumerate(names,start=1):
	print(index, name)