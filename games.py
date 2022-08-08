1.##Guess Game

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Sorry, you failed!!')


2.## Car Game:

command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
            if started:
               print("Car already started!!!")
            else:
               started = True
               print("Car started")
    elif command == "stop":
        if not started:
            print("Car is already stopped!!")
        else:
            started = False
            print("Car stopped.")
        print("Car stopped!")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quite":
        break
    else:
        print("I don't understand That")


3. ##calculate items in shopping cat
prices = [20, 40, 50]
total = 0
for item in prices:
    total += item
print(f'total {total} ')

4.## largest Number
numbers = [7, 8,3, 0, 7, 35, 23, 6]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

4.## Remove doublicate
numbers = [7, 8,3, 6, 7, 35, 23, 6]

uniques = []
for item in numbers:
    if item not in uniques:
        uniques.append(item)
print(uniques)


5. ## Dice game
import random

class Dice:
    def roll(self):
        first = random.randint(2, 8)
        second = random.randint(2, 8)
        return first, second

dice = Dice()
print(dice.roll())
