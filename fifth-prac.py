name = 'aditya'
name_len = len(name)

if name_len <= 3 :
	print('name must be at least 3 characters')
elif name_len >= 50 :
	print('name can be maximum of 50 characters')
else :
	print('name looks good')