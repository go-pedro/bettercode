# #normal method
# username=input('username: ')
# password=input ('password: ')

# print('loggin in...')

#with getpass method
from getpass import getpass

username=input('username: ')
password=getpass('password: ')

print('loggin in...')