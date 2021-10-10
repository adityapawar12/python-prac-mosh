started = False

while True :
    command = input('> ').upper()
    if command == 'HELP' :
        print('start : to start the car.')
        print('stop : to stop the car.')
        print('quit : to exit the game.')
    elif command == 'START' :
        if started :
            print('car already started')
        else :
            started = True
            print('car started...')
    elif command == 'STOP' :
        if not started :
            print('car already stopped')
        else :
            started = False
            print('car stopped....')
    elif command == 'QUIT' :
        break
    else :
        print("i don't understand that")
        