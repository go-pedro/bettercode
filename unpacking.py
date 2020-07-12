#normal
items=(1,2)
print (items)

#unpacking
a,b=(1,2)

print(a)
print(b)

#unpacking
a,_=(1,2)  # use _ to ingnore some values when unpacking

print(a)
#print(b)

#unpacking
a,b,*c=(1,2,3,4,5)  # use _ to ingnore some values when unpacking

# or *_ #ignore all the remaind values
print(a)
print(b)
print(c)

#unpacking
a,b,*c,d=(1,2,3,4,5)
print(a)
print(b)
print(c)
print(d)