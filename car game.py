help = ""
started = False
while True:
    help = input("> ").lower()  # <-- fix here
    if help == "start":
        if started:
            print('car is already started')
        else:
            started = True
            print('car started')
    elif help == "stop":
        if not started:
            print('car is already stopped')
        else:
            started = False
            print('car stopped')
    elif help == "help":
        print("""
start - to start the car
stop  - to stop the car
quit  - to quit
        """)
    elif help == 'quit':
        break
    else:
        print('i dont understand')