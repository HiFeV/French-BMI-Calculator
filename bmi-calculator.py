#coding-utf8
import os 
import re

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

taille = input('Entrez votre taille en mètres: ')
regex1 = re.match('^[0-9\.]*$',taille)

while regex1 == None:
    cls()
    print('Saisie Invalide...')
    taille = input('Entrez votre taille en mètres: ')
    regex1 = re.match('^[0-9\.]*$',taille)
taille = float(taille)

masse = input('Entrez votre masse en kilogrammes: ')
regex2 = re.match('^[0-9\.]*$',masse)

while regex2 == None:
    cls()
    print('Saisie Invalide...')
    masse = input('Entrez votre masse en kilogrammes: ')
    regex2 = re.match('^[0-9\.]*$',masse)
masse = float(masse)



anorexie = 'Dénutrition ou Anorexie détectées.'
maigreur = 'Maigreur détectée.'
normal = 'Aucun soucis détecté.'
surpoids = 'Surpoids détecté.'
obésité_1 = 'Obésitée modérée détectée'
obésité_2 = 'Obésitée sévère détectée.'
obésité_3 = 'Obésité morbide détectée.'


imc = masse/(taille**2)

if imc < 16.5:
    print('Votre IMC est de ',imc,': {}'.format(anorexie))

elif imc > 16.5 and imc < 18.5:
    print('Votre IMC est de ',imc,': {}'.format(maigreur))

elif imc > 18.5 and imc < 25:
    print('Votre IMC est de ',imc,': {}'.format(normal))

elif imc > 25 and imc < 30:
    print('Votre IMC est de ',imc,': {}'.format(surpoids))

elif imc > 30 and imc < 30:
    print('Votre IMC est de ',imc,': {}'.format(obésité_1))

elif imc > 35 and imc < 40:
    print('Votre IMC est de ',imc,': {}'.format(obésité_2))

elif imc > 40:
    print('Votre IMC est de ',imc,': {}'.format(obésité_3))