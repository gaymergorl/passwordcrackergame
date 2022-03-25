import random
import numpy
number = range(0, 9)
colour = ["red", "blue", "green","pink", "grey", "orange", "yellow"]
animal = ["dog","cat", "monkey", "fish", "capybara", "snake", "gecko", "bee"]
from numpy import *
def comb(a , b , d):
    c = []
    for i in a:
        for j in b:
            for s in d:
                c.append(r_[i,j])
    return c

def combs(a,m):
    return reduce(comb,[a]*m)
    values = combs(np.arange(0,1,0.1),6)

for val in values:
    print(val)