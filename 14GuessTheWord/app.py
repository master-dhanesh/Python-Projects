import random
import os

def wordpicker():

    with open ("words.txt","r") as word:
        words = word.readlines()
    w = words[random.randint(0,len(words))]
    x = w.split("\n")
    return x[0]

def hangman(tries):
    print()
    arr = [[" "," ","O"],["\n","--"],["|"],["--","\n"],["  ","|"],["\n"," ","/"],[" ","\\"],[""]]
    for i in range(tries):
        for j in range(len(arr[i])):
            print(arr[i][j],end="")

def printer(l):


    for i in range(len(l)):
        print(l[i],end=" ")
    print()

word = wordpicker()
tries = 0
chance = 8
g = set()
l = ["_" for i in range(len(word))]
printer(l)

while tries != chance:

    if word.upper() == "".join(l):
        print("\nYaaa! you saved me!\n")
        break
    print("Guess the word?")
    guess = input("\nEnter Guess Letter: ")
    os.system("cls")
    g.add(guess)
    if len(g) > 0:
        for i in g:
            print("(",end="")
            print(i,end="") 
            print(")",end="")
    print("\n")

    if guess in word:    
        index = [i for i, l in enumerate(word) if l == guess]
        for i in index:
            l[i] = guess.upper()
        hangman(tries)
        print()
        print()
        printer(l)

    if guess not in word:
        tries+=1
        hangman(tries)
        print()
        print()
        printer(l)
else:
    print("\ni trusted you...")
    print("The word was,",word,"\n")