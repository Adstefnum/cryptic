from general import *

mode = input("Would you like to \n 1 - encrpyt or \n 2 - decode:")
encrypt_type = input('What type of encryption would you like(binary,atbash):')

values = dict_picker(encrypt_type)
encoded = execute(values,encrypt_type,mode)
print(encoded)
