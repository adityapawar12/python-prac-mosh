weight = input('enter your weight : ')
print('if you entered your weight in lbs type l')
print('and if you entered your weight in kg type k')
unit = input("(l)bs or (k)g : ")

if unit.upper() == 'L' :
	print('your weight in kilogram is : ', float(weight) / 2.205)
elif unit.upper() == 'K' :
	print('your weight in pounds is : ', float(weight) * 2.205)

# other way
#if unit.upper() == 'L' :
#	print('your weight in kilogram is : ', float(weight) * 0.45)
#elif unit.upper() == 'K' :
#	print('your weight in pounds is : ', float(weight) / 0.45)
