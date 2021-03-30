from math import *
from easygui import *
# Cours 2 (1

# chiffre = float(input('Insérer un chiffre '))

# if chiffre >= 0:
#     print(sqrt(chiffre))
# else:
#     print('Erreur')

# Cours 2 (2

# first_word = input('Saisir un mot ')
# second_word = input('Saisir un autre mot ')

# if first_word < second_word:
#     print(first_word)
# elif second_word < first_word:
#     print(second_word)
# else:
#     print('Mot de même mot')

# res = first_word if first_word<second_word else second_word if second_word<first_word else 'Même mot'
# print(res)

# Cours 2 (3

# pSeuil = 2.3
# vSeuil = 7.41
# pression = float(input("Insérer la pression de l'enceinte" ))
# volume = float(input("Insérer le volume de l'enceinte" ))

# if volume > vSeuil and pression > pSeuil:
#     print('Arrèt immédiat')
# elif pression > pSeuil and volume <= vSeuil:
#     print("Augmenter le volume de l'enceinte")
# elif volume > vSeuil and pression <= pSeuil:
#     print("Diminuer le volume de l'enceinte")
# else:
#     print('tout vas bien')

# Cours 2 (4

# a=0
# b=10

# while a<b:
#     a+=1
#     print(a)
# while b != 0:
#     b -= 1
#     if b%2 == 1:
#         print(b)

# Cours 2 (5

# liste = [1,2,3,4,5,6,7,8,9,10]
# choix = int(input('Choisissez un nombre '))
# if choix in liste:
#     print('Le nombre choisi est ', choix)
# else:
#     print('Nombre pas dans la liste')

# Cours 2 (6

# chaine = input('Insérer une chaine de caractère ')
# liste = ["la", "baignoire", "est", "dans", "l'ananas" ]

# for i in range(len(chaine)):
#     print(chaine[i])
# for y in range(len(liste)):
#      print(liste[y])

# Cours 2 (7

# for i in range(15):
#     if (i%3)==0:
#         print(i)

# Cours 2 (8

# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)

# Cours 2 (9

# for i in range(1, 11):
#     if i ==5:
#         continue
#     print(i)

# Cours 2 (10

# for i in range(-3, 4):
#     if i != 0:
#         sin(i)/i
#         print(i)

# Cours 2 (11 


sauvegarde = []
liste = [48, 75, 28, 83, 2]
number = integerbox("Choisissez un entier: ")
isPrime = False
flag=False

for i in range(len(liste)):
    if number in liste:
        sauvegarde.append(number)
        msgbox('Bien joué, vous avez trouvé un nombre.' + str(sauvegarde))
        break
else:
    msgbox("Le nombre choisis n'est pas dans la liste")  

number2 = integerbox("Choisissez un autre entier, positif: ")

while isPrime != True:
    if number2 > 1:
        for i in range(2, number2):
            if (number2 % i )== 0:
                diviseur = i
                flag = True
                break
    isPrime=True

if flag:
    msgbox("Ce n'est pas un nombre premier et son diviseur est " + str(diviseur))
else:
     msgbox("C'est un nombre premier")

