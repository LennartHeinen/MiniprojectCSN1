import csv
import random
import RPi.GPIO as GPIO
import time

# variabelen van led lampjes en button
led_pin_red = 19
led_pin_green = 22
button_pin_true = 21
button_pin_false = 12

# setup van knopjes en lampjes
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin_red, GPIO.OUT)
GPIO.setup(led_pin_green, GPIO.OUT)
GPIO.setup(button_pin_true, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_pin_false, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# functie gebruikersnaam
def gebruiker():
    gebruiker = raw_input('Wat is je naam?')
    return gebruiker
# functie keuzemenu
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

# functie uitlezen csv file
def quiz(quizFile):
    score = 0
    bestand = quizFile
    vragen = csv.DictReader(open(bestand, 'r'), delimiter=',')
    vragenLijst = []

    for line in vragen:
        vragenLijst.append(line)

    random.shuffle(vragenLijst)
# uitwerking quiz
    while True:
        for i in range(len(vragenLijst)):
            print(vragenLijst[i]['nummer'], vragenLijst[i]['vraag'])
            goedAntwoord = vragenLijst[i]['antwoord']

            while True:
                if GPIO.input(button_pin_true):
                    antwoord = 'WAAR'

                    if antwoord == str(goedAntwoord):
                        GPIO.output(led_pin_red, True)
                        time.sleep(2)
                        GPIO.output(led_pin_red, False)
                        print('Goed')
                        score += 1
                    else:
                        GPIO.output(led_pin_green, True)
                        time.sleep(2)
                        GPIO.output(led_pin_green, False)
                        print('Fout')
                    time.sleep(0.2)
                    break

                elif GPIO.input(button_pin_false):
                    antwoord = 'ONWAAR'
                    if antwoord == str(goedAntwoord):
                        GPIO.output(led_pin_red, True)
                        time.sleep(2)
                        GPIO.output(led_pin_red, False)
                        print('Goed')
                        score += 1
                    else:
                        GPIO.output(led_pin_green, True)
                        time.sleep(2)
                        GPIO.output(led_pin_green, False)
                        print('Fout')
                    time.sleep(0.2)
                    break

        return score

# functie eindscore
def uitslag(naam, punten):

	if punten == 25:
		print ('Gefeliciteerd '+ naam + ', jij bent echt een swekkerdekker! '+ str(punten)+'/25')
	else:
		print(naam + ' heeft ' + str(punten) + ' gehaald!')
try:
	naam = gebruiker()
	quizFile = menu()
	punten = quiz(quizFile)
	uitslag(naam, punten)
except KeyboardInterrupt:
	print('tot ziens')
