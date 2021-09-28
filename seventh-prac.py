secret_num = 5
guess_count = 0
guess_limit = 3

while guess_count < guess_limit :
    guess = int(input('guess the number : '))
    
    if secret_num == guess :
        print('you guessed it')
        print('congrats you won')
        break
    else :
        print('you missed it') 
        
    guess_count += 1
    
else :
        print('sorry you lost')