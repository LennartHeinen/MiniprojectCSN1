print('Hello world')
print('Hello world2')
print('Hallo')
print('Hello World3')
print(' ')

import csv


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

Quiz()






