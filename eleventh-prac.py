# my solution

numbers = [3, 2, 5, 3, 1, 6, 9, 6]
print(numbers)

for number in numbers :
    count = numbers.count(number)
    print(count)
    if count > 1 :
        numbers.remove(number)
        
print(numbers)


# mosh's solution

numbers = [2, 2, 4, 7, 3, 5, 3, 6]
uniques = []

print(numbers)

for number in numbers :
    if number not in uniques :
        uniques.append(number)

print(uniques)