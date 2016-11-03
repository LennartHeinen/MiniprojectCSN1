import csv
import random
import RPi.GPIO as GPIO
import time

# variabelen van led lampjes en button
led_pin = 19
led_pin2 = 22
button_pin = 21
button_pin2 = 12

# setup van
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_pin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def gebruiker():
    gebruiker = raw_input('Wat is je naam?')
    return gebruiker

def menu():

    while True:
        keuze = int(input('kies 1 voor dieren Quiz en 2 voor sport quiz'))
        print(keuze)
        if keuze == 1:
            bestand = '25_vragen_dieren.csv'
            break
        elif keuze == 2:
            bestand = 'Sport_vragen.csv'
            break
        else:
	    print('Ongeldige keuze!')
            continue
    return bestand


def quiz(quizFile):
    score = 0
    bestand = quizFile
    vragen = csv.DictReader(open(bestand, 'r'), delimiter=',')
    vragenLijst = []

    for line in vragen:
        vragenLijst.append(line)

    random.shuffle(vragenLijst)

    while True:
        for i in range(len(vragenLijst)):
            print(vragenLijst[i]['nummer'], vragenLijst[i]['vraag'])
            goedAntwoord = vragenLijst[i]['antwoord']

            while True:
                if GPIO.input(button_pin):
                    antwoord = 'WAAR'

                    if antwoord == str(goedAntwoord):
                        GPIO.output(led_pin, True)
                        time.sleep(2)
                        GPIO.output(led_pin, False)
                        print('Goed')
                        score += 1
                    else:
                        GPIO.output(led_pin2, True)
                        time.sleep(2)
                        GPIO.output(led_pin2, False)
                        print('Fout')
                    time.sleep(0.2)
                    break

                elif GPIO.input(button_pin2):
                    antwoord = 'ONWAAR'
                    if antwoord == str(goedAntwoord):
                        GPIO.output(led_pin, True)
                        time.sleep(2)
                        GPIO.output(led_pin, False)
                        print('Goed')
                        score += 1
                    else:
                        GPIO.output(led_pin2, True)
                        time.sleep(2)
                        GPIO.output(led_pin2, False)
                        print('Fout')
                    time.sleep(0.2)
                    break

        return score


def uitslag(naam, punten):

	if punten == 25:
		print ('Gefeliciteerd '+ naam + ', jij bent echt een swaggerdekker! '+ str(punten)+'/25')
	else:
		print(naam + ' heeft ' + str(punten) + ' gehaald!')
try:
	naam = gebruiker()
	quizFile = menu()
	punten = quiz(quizFile)
	uitslag(naam, punten)
except KeyboardInterrupt:
	print('tot ziens')
