import random
number = str(random.randint(1,9))
colour = ["red", "blue", "green","pink", "grey", "orange", "yellow"]
animal = ["dog","cat", "monkey", "fish", "capybara", "snake", "gecko", "bee"]

passcolour = colour[random.randint(0,len(colour) - 1)]
passanimal = animal[random.randint(0,len(animal) - 1)]
password = passcolour + passanimal + number