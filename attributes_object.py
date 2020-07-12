class Person():
	pass

person=Person()

# #set attributes to an object
# person.first='pedro'
# person.last='goncalves'

# print(person.first)
# print(person.last)

first_key='first'
first_value='pedro'

# person.first_key=first_value  ## does not work!!
#using get attribute
#setattr(person,'first','pedro')
#=
setattr(person,first_key,first_value)

print(person.first)

first=getattr(person,first_key)
print(first)

#öooping through a dictionary
person_info={'fisrt':'pedro', 'last':'goncalves'}

for key, value in person_info.items():
	setattr(person,key,value)

print(person.first)
print(person.last)

for key in person_info.keys():
	print(getattr(person,key))
