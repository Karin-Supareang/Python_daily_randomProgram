# try using: random lib, random(), list , index(), and \"Quotationmark\" 
import random

joke =[ "I went to the aquarium this weekend, but I didn’t stay long.", "Why can’t orphans play baseball?", "I visited my new friend in his apartment. He told me to make myself at home.", "Do you know the phrase \"One man's trash is another man's treasure\"?", "Give a man a match, and he'll be warm for a few hours."]
punchline = [ "There’s something fishy about that place.", "They don’t know where home is.", "So I threw him out. I hate having visitors.", "It's a wonderful saying but a horrible way to find out that you were adopted.", "Set him on fire, and he will be warm for the rest of his life."]
randomNoise = ["Duh", "womp womp", "Bruh", "Nihaha", "Huh", "Lol", "Wheez"]

user_answer = ""
tempAnswer = ""
user_answer = input("Wanna hear some jokes? (type no to excape): ")
while not user_answer == "no":

    tellJoke = random.choice(joke)
    punchlineIndex = joke.index(tellJoke)
    make_noise = random.choice(randomNoise)
    user_answer = user_answer.lower()
    print(f"Ok, here some joke. {tellJoke}")
    user_answer = input("your respond (can escape): ")
    print(f"{punchline[punchlineIndex]} {make_noise}")
    user_answer = input("Wanna hear some more jokes? (type no to excape): ")
    
print("Welp, that will be all for todays folk.")