#Ćwiczenie 7 str 179
#podanie dwóch podstawowych kolorów wyświetli kolor powstały z wymieszania obydwu
#Dodane wymagania co do komunikatach o błędach.

col1 = str(input('Podaj nazwę pierwszego koloru: '))
col2 = str(input('Podaj nazwę drugiego koloru: '))

error = 'Podane kolory są identyczne.'
error1 = 'Podano błędny kolor 1.'
error2 = 'Podano błędny kolor 2.'

violet = (col1 != col2) and (col1 == 'czerwony' or col1 == 'niebieski') and (col2 == 'czerwony' or col2 == 'niebieski')
orange = (col1 != col2) and (col1 == 'czerwony' or col1 == 'żółty') and (col2 == 'czerwony' or col2 == 'żółty')
green = (col1 != col2) and (col1 == 'żółty' or col1 == 'niebieski') and (col2 == 'żółty' or col2 == 'niebieski')


if not(col1 == 'czerwony' or col1 == 'niebieski' or col1 == 'żółty'):
    print(error1)
    if not(col2 == 'czerwony' or col2 == 'niebieski' or col2 == 'żółty'):
        print(error2)
        if col1 == col2:
            print(error)  
##else:
##    if not(col2 == 'czerwony' or col2 == 'niebieski' or col2 == 'żółty'):
##        print(error2)
##    if col1 == col2:
##        print(error)
##    if violet:
##        print('Po wymieszaniu powstanie fioletowy.')
##    if orange:
##        print('Po wymieszaniu powstanie pomarańczowy.')
##    if green:
##        print('Po wymieszaniu powstanie zielony.')

else:
    if not(col2 == 'czerwony' or col2 == 'niebieski' or col2 == 'żółty'):
        print(error2)
    else:
        if col1 == col2:
            print(error)
        if violet:
            print('Po wymieszaniu powstanie fioletowy.')
        if orange:
            print('Po wymieszaniu powstanie pomarańczowy.')
        if green:
            print('Po wymieszaniu powstanie zielony.')
