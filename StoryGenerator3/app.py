import random
from time import sleep

mainChar = input("Main Character: ")
rivalName = input("Rival's Name: ")
activity = input("Daily activity(e.g. watching TV): ")
posAdj = input("Positive adjective (e.g. funny, happy): ")
negAdj = input("Negative adjective (e.g. Careless, Dishonest): ")

word1 = ['question', 'code', 'comment']
word2 = ['penguins', 'programmer jokes', 'text generation', 'another amazing fireworks','finding your partner']
word3 = ['Python', 'Java', 'JavaScript', 'C', 'UI/UX', 'Code']
word4 = ['liked', 'disliked', 'reported', 'deleted']

Sentance = [
    'Yesterday, while browsing Sheryians Coding School, and', 'activity', ',',
    'mainChar', 'noticed that', 'rivalName', 'posted a new', 'word1', 'about',
    'word2', '. He', 'word4', 'it and challenged him to a', 'word3',
    'battle. Then he posted his own', 'posAdj', 'word1', ', but', 'rivalName',
    'retailated', 'negAdj', 'word1', 'about', 'word2', '.'
]

for item in Sentance:
    if item == 'activity': Sentance[Sentance.index(item)] = activity
    elif item == 'mainChar': Sentance[Sentance.index(item)] = mainChar
    elif item == 'rivalName': Sentance[Sentance.index(item)] = rivalName
    elif item == 'posAdj': Sentance[Sentance.index(item)] = posAdj
    elif item == 'negAdj': Sentance[Sentance.index(item)] = negAdj

    elif item == 'word1': Sentance[Sentance.index(item)] = random.choice(word1)
    elif item == 'word2': Sentance[Sentance.index(item)] = random.choice(word2)
    elif item == 'word3': Sentance[Sentance.index(item)] = random.choice(word3)
    elif item == 'word4': Sentance[Sentance.index(item)] = random.choice(word4)
    else: continue

story = " ".join(item for item in Sentance)
print('We are generating story, please wait.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)
print(story)