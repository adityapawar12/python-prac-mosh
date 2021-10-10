# my solution took a hint
request = input("please enter your phone number : ")
user = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}

for i in request :
    print(user.get(i))    

# mosh's solution

phone = input("phone: ")
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"    
}
output = ""
for ch in phone :
    output += digits_mapping.get(ch, "!") + " "
    
print(output)