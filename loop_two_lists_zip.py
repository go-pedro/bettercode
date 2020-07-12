names=['peter parker', 'clark kent', 'wade wilson', 'bruce wayne']
heroes=['spiderman', 'superman', 'dedpool', 'batman']
universes=['Marvel','DC','Marvel','DC']

# # old code
# for index, name in enumerate (names):
# 	hero=heroes[index]  
# 	print(f'{name} is actually {hero}')

for name, hero, universe in zip(names, heroes, universes):
	print(f'{name} is actually {hero} from {universe}')

#print tupple of 3 values
for value in zip(names, heroes, universes):
	print(value)
