# functions

## function without parameters

def greet():
  print("Hello!!")

'''
greet()
'''

## function with parameters

def sayHi(name):
  print("Hi "+ name)

'''
sayHi("Ava")
sayHi("Eva")
sayHi("Eve")
sayHi("Guzel")
'''

## function with library

import random

def complimentGenerator(name):

    adjectives = ["brilliant", "sparkling", "charming", "fearless"]
    talents = ["solving code bugs", "dancing through life", "making people smile",
               "turning coffee into code", "creating masterpieces"]
    quirks = ["the heart of an adventurer", "an endless imagination",
              "the curiosity of a cat", "the charm of a storyteller"]

    compliment = (
        f"{name}, you are as {random.choice(adjectives)} as they come, "
        f"with a gift for {random.choice(talents)} and {random.choice(quirks)}!"
    )
    
    return compliment

print(complimentGenerator("Ava"))
