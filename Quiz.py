print('Hello world')
print('Hello world2')
print('Hallo')
print('Hello World3')
print(' ')

import csv
import random


def Quiz():
    Quizfile = open('Quizantwoorden.csv', 'r')
    Quizvragen = open('Quizvragen.csv', 'r')

    A = True
    while A == True:
        Vraag = Quizvragen.readline()
        GoedAntw = Quizfile.readline()
        GoedAntw = GoedAntw.replace('\n','')

        antwoord = str(input('Is dit True of False? :'))
        if antwoord == GoedAntw:
            print('Je hebt het antwoord goed')
        else:
           print('Je hebt het antwoord fout')
        if Vraag == '':
            A = False

def sportVragen ():
    quizFile = 'Sport_vragen.csv'
    vragen = csv.DictReader(open(quizFile,'r'),delimiter=',')
    vragenLijst = []
    for line in vragen:
        vragenLijst.append(line)
    print(vragenLijst)

    random.shuffle(vragenLijst)
    print(vragenLijst)

    punten = 0
    for i in range(len(vragenLijst)):
        print(vragenLijst[i]['nummer'], vragenLijst[i]['vraag'])
        antwoord = str(input('Is True or False'))
        goedAntwoord = vragenLijst[i]['antwoord']
        while button_pressed:
            if antwoord == str(goedAntwoord):
                print('Goedzo noob')
            else:
                print('Fout sukkel')

def randomQuiz():

    dict = [{'Nummer': 1, 'vraag': 'Is koen een geit?', 'antwoord': True},
            {'Nummer': 2, 'vraag': 'Is Roy een koe?', 'antwoord': True},
            {'Nummer': 3, 'vraag': 'Is Chung een kip?', 'antwoord': True},
            {'Nummer': 4, 'vraag': 'Stinken we?', 'antwoord': False},
            {'Nummer': 5, 'vraag': 'Wordt PSV kampioen?', 'antwoord': False}]

    random.shuffle(dict)
    print(dict)

    for i in range(len(dict)):
        print(dict[i]['Nummer'], dict[i]['vraag'])
        antwoord = str(input('Is True or False'))
        goedAntwoord = dict[i]['antwoord']
        print(type(goedAntwoord))
        if antwoord == str(goedAntwoord):
            print('Goedzo noob')
        else:
            print('Fout sukkel')

sportVragen()
#Quiz()
#randomQuiz()

