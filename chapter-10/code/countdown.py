
def countdown(number):
    if number == 0:
        print("Liftoff!")
        return
    print(number)
    countdown(number - 1)
    
countdown(5)

countdown(7)
