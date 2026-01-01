import random

greeting = ["Hello", "Hola", "Bonjour", "Guten Tag", "Konnichiwa", "Hai", "Welcome Aboard", "Greetings", "Welcome", "Ciao"]

def getGreeting():
    setIndex = random.randint(0,(len(greeting) - 1))
    setGreeting = greeting[setIndex]
    return setGreeting