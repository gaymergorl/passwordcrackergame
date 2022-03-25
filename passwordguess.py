import random
number = str(random.randint(1,3))
colour = ["red", "blue", "green"]
animal = ["dog","cat", "monkey"]
guessed = False
passcolour = colour[random.randint(0,len(colour) - 1)]
passanimal = animal[random.randint(0,len(animal) - 1)]
password = passcolour + passanimal + number
guesscounter = 0
print("Try to guess the password!")
print('Hint: the password follows the format "colour, animal, number" ')
while guessed == False:
    guess = input()
    if guess == password:
        print("Well done you guessed the password!")
        guessed = True
    else:
        print("try again")
        guesscounter = guesscounter + 1
print("Well done you got it in ",guesscounter,"tries")