#"""Paradoks dnia urodzin, autor: Al Sweigart, al@inventwithpython.com
 #Odkryj zaskakujące prawdopodobieństwa paradoksu dnia urodzin.
 #Więcej informacji na stronie https://en.wikipedia.org/wiki/Birthday_problem.
 #Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
 #Etykiety: krótki, matematyka, symulacja"""

import datetime, random
from urllib import response


def getBirthdays(numberOfBirthdays):
    """Zwraca listę losowych dni urodzin"""
    birthdays = []
    for i in range(numberOfBirthdays):
        # Rok nie jest ważny dla naszej symulacji, jeśli tylko dni urodzin 
        # # wypadają w tym samym roku.
        startOfYear = datetime.date(2022, 1, 1)

        # Wylosuj dzień w roku:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    '''Zwraca date urodzin, która pojawia się wiecej ni raz
    w liście urodzin'''
    if len(birthdays) == len(set(birthdays)):
        return None # Wszystkie dni są unikatowe, dlatego zwróć None.
    
    # Porównaj kade urodziny z pozostałymi:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA # Zwróć takie same urodziny.


#Wyświetl wstęp:
print('''Paradoks dnia urodzin, autor: Al Sweigart

Paradoks dnia urodzin pokazuje,ze w grupie N osób szansa,
że dwie osoby mają urodziny w tym samym dniu, jest zaskakująco duża.
Ten program wykorzystuje metodę Monte Carlo (czyli powtarzalne losowe
symulacje), by ustalić to prawdopodobieństwo.

(To tak naprawdę nie jest paradoks, tylko zaskakujący wynik.)
''')

#Deklaracja krotki z miesiącami:
MONTHS = ('Styczeń', 'Luty', 'Mar', 'Kwi', 'Maj', 'Cze',
        'Lip', 'Sie', 'Wrz', 'Paź', 'Lis', 'Gru')

while True: #Pytaj, dopóki uzytkownik nie poda odpowniedniej wartości.
    print('Ile urodzin powinienem wygenerować? (Maks. 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break #Uzytkownik podał odpowiednią wartość.
print()

#Wygeneruj i wyświetl dni urodzin:
print('Oto', numBDays, 'dni urodzin:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        #Po pierwszym dniu urodzin wyświetl przecinek.
        print(', ', end='')
    monthName =  MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

#Sprawdź, czy są takie same dni urodzin. 
match =  getMatch(birthdays)

#Wyświetl wynik:
print('W tej symulacji, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('Kilka osób ma urodziny', dateText)
else:
    print('nie ma takich samych dni urodzin.')
print()

#Przeprowadzono 100 000 symulacji:
print('Generowanie ', numBDays, 'losowych dni urodzin 100 000 razy ...')
input('Naciśnij Enter, aby rozpocząć...')

print('Przeprowadźmy kolejnych 100 000 symulacji.')
simMatch = 0 #Liczba symulacji w których wystąpiły te same dni urodzin.
for i in range(100_000):
        # Wyświetlanie postępu co 10 000 symulacji
    if i % 1_000 == 0:
        print(i, 'przeprowadzonych symulacji...')
        birthdays = getBirthdays(numBDays)
        if getMatch(birthdays) != None:
            simMatch = simMatch + 1
print('100 000 przeprowadonych symulacji.')

#Wyświetlanie wyników symualcji:
probability = round(simMatch / 100_000 * 100, 2)
print('Ze 100 000 symulacji dla ', numBDays, 'osób, ten sam') 
print('dzień urodzin wystąpił', simMatch, 'razy. Oznacza to,')
print('że dla ', numBDays, 'ludzi istnieje ', probability, '% szans, iż') 
print('dwie lub więcej osób będzie miało urodziny w tym samym dniu.') 
print('To prawdopodobnie więcej, niż przypuszczałeś!')
