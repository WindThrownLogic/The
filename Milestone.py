from random import randint

number = randint(0, 20)

def check(user_number):
    if user_number > number:
        return "high"
    elif user_number < number:
        return "low"
    elif user_number == number:
        return "yes"
    
def guess():
    print("Guess a number")
    answer = int(input())
    if check(answer) is 'yes':
        print("You guessed it!")
        return('yes')
    else:
        print("Close! You're too", check(answer))

def game(done='no'):
    while done is 'no':
        if guess() is 'yes':
            break

game()
