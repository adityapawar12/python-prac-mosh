num_list = [2, 4, 43, 23 , 44, 643]

#my solution
prev_num = 0
great_num = 0

for num in num_list :
    if great_num > num :
        great_num = prev_num
    elif num > great_num :
        great_num = num
    prev_num = num
    
print(great_num) 

# mosh's solution

numbers = [2, 3, 5, 3, 6, 9]
max = numbers[0]
for number in numbers :
    if number > max :
        max = number
print(max)