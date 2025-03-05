import inquirer
import random

def StartGame():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 chances to guess the correct number.\n")

StartGame()

questions = [
  inquirer.List('answer',
                message="Please select the difficulty level(Use arrow keys to select answer)",
                choices=['1. Easy (10 chances)','2. Medium (5 chances)', '3. Hard (3 chances)'],
            ),
]

answer = inquirer.prompt(questions)

def RandomNumberGenerator(attemps):
    number = random.randint(1,100)
    if attemps == 10:
        for counter in range(1,11):
            answer = int(input('Enter your choice : '))
            if answer == number:
                print(f'Congratulations! You guessed the correct number in {counter} attempts.')
                break
            else:
                if counter == 10:
                    print(f"Sorry! You've used all {attemps} attempts. The correct number was {number}.")
                    break
                else:
                    if answer < number:
                        print(f'Incorrect! The number is greater than {answer}.')
                        counter +=1
                    elif answer > number:
                        print(f'Incorrect! The number is less than {answer}.')
                        counter +=1
    elif attemps == 5:
        for counter in range(1,6):
            answer = int(input('Enter your choice : '))
            if answer == number:
                print(f'Congratulations! You guessed the correct number in {counter} attempts.')
                break
            else:
                if counter == 5:
                    print(f"Sorry! You've used all {attemps} attempts. The correct number was {number}.")
                    break
                else:
                    if answer < number:
                        print(f'Incorrect! The number is greater than {answer}.')
                        counter +=1
                    elif answer > number:
                        print(f'Incorrect! The number is less than {answer}.')
                        counter +=1
    elif attemps == 3:
        for counter in range(1,4):
            answer = int(input('Enter your choice : '))
            if answer == number:
                print(f'Congratulations! You guessed the correct number in {counter} attempts.')
                break
            else:
                if counter == 3:
                    print(f"Sorry! You've used all {attemps} attempts. The correct number was {number}.")
                    break
                else:
                    if answer < number:
                        print(f'Incorrect! The number is greater than {answer}.')
                        counter +=1
                    elif answer > number:
                        print(f'Incorrect! The number is less than {answer}.')
                        counter +=1
                      
for e in answer.values():
    if e == '1. Easy (10 chances)':
        print('Great! You have selected the Easy difficulty level.')
        print("Let's start the game!")
        RandomNumberGenerator(10)
    elif e == '2. Medium (5 chances)':
        print('Great! You have selected the Medium difficulty level.')
        print("Let's start the game!")
        RandomNumberGenerator(5)
    elif e == '3. Hard (3 chances)':
        print('Great! You have selected the Hard difficulty level.')
        print("Let's start the game!")
        RandomNumberGenerator(3)




