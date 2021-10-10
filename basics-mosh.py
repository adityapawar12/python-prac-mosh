# modules import
import math


# print function practice
print('heart')
print('*' * 10)
variable_name = 10


# data types in python
int_value = 10
float_value = 1.1
str_value = 'string'
bool_value = True

print(variable_name)


# input statement practice
#your_name = input('enter your name : ')
#print('your name is ' + your_name)

#birth_year = input('enter your year of birth : ')
#age = 2021 - int(birth_year)
#print(age)
#print(type(age))


# string practice
string_name = "a python string with an ' apostophe"
mult_string = '''
	a
	multiline 
	string
	
'''
print(string_name)
print(mult_string)
print(string_name[0])
print(string_name[-1])
print(string_name[0:4])
print(string_name[:])
print(string_name[1:-1])


# string formatting practice
first = 'aditya'
last = 'pawar'

msg = 'my name is ' + first + ' [' + last + '] '
f_msg = f'my name is {first} [{last}]'

print(msg)
print(f_msg)


# string module methods
print(len(f_msg))
print(f_msg.upper())
print(f_msg.lower())
print(f_msg.title())
print(f_msg.find('name'))
print(f_msg.replace('name', 'NAME'))
print('my' in f_msg)


# arithmetic operators in python
expression = 16 + 3 * 4 / 8 // 4 ** (2 - 4)
print(expression)


# math function examples
m_var = 2.8
print(round(m_var), " ", abs(m_var) , " ", math.ceil(m_var), " ", math.floor(m_var))


# if statement in python
is_hot = True
is_cold = False

if is_hot :
	print('it is a hot day')
elif is_cold :
	print('it is a cold day')
else :
	print('it is a nice day')

		
# logical operators
has_high_income = True
has_good_credit = True
has_crim_record = False

if has_high_income and has_good_credit :
	print('eligible for loan')

if has_high_income or has_good_credit :
	print('can be eligible for loan')

if has_high_income and not has_crim_record :
	print('eligible for loan')
	
	
# comparison operators
temperature = 15
if temperature >= 30 :
	print("it's a hot day")
elif temperature <= 10 :
	print("it's a cold day")
else :
	print("it's a nice day")
	

# while loop
w_num = 0
while w_num < 3 :
    print('*' * w_num)
    w_num += 1
    
print('done')

# for loop
for_str = "py"
for_list = ["p", "y"]
for_range = range(1, 2, 1)

for letter in for_str:
    print(letter)
    
for name in for_list :
    print(name)
    
for num in for_range :
    print(num)


# nested loops

for x in range(1, 4) :
    for y in range(1, 3) :
        print(f"({x} {y})")