# my solution 
f_list = [5, 2, 5, 2, 2]
letter = "X"
seq = ''
for num in f_list :
    for n in range(num):
        n = letter
        seq += str(n)
    print(seq) 
    seq =""
        
print(seq)

# mosh solution 

numbers = [2, 2, 2, 2, 5]
for x_count in numbers :
    output = ""
    for count in range(x_count) :
        output += "X"
    print(output)