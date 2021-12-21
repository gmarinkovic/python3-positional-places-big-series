# Уносе се природни бројеви (укључујући и 0) док се не унесе -1. Међу унетим бројевима који садрже бар
# једну парну цифру, наћи најмањи број са највећим збиром парних цифара.
#
# Улаз: Линије стандардног улаза, њих највише милион, садрже по један природан број. Последња линија
# стандардног улаза садржи број -1.
#
# Излаз: Прва и једина линија стандардног излаза садржи најмањи број од унетих бројева са највећим збиром
# парних цифара. Ако међу унетим бројевима нема оних који садрже парне цифре, на излазу приказати -1.
#
# Пример 1
# Улаз
# 137
# 20
# 143
# 221
# 0
# 22
# 4
# -1
# Излаз
# 4
#
# Пример 2
# Улаз
# 137
# 39
# 155
# 791
# 731
# 31
# -1
# Излаз
# -1

# vraća True ako i samo ako n sadrži bar jednu parnu cifru u svom dekadnom zapisu
def ima_parnih_cifara(n):
    while True:
        if n % 2 == 0:
            return True
        n = n // 10
        if n == 0:
            break
    return False

# izračunava zbir parnih cifara broja n
def zbir_parnih_cifara(n):
    zbir = 0
    while True:
        if n % 2 == 0:
            zbir = zbir + n % 10
        n = n // 10
        if n == 0:
            break
    return zbir


# max - najbolji do sada procitani broj (najmanji broj sa najvecim zbirom parnih cifara)
max = -1
postavljen_max = False                              # da li je pronađen neki broj sa parnim ciframa

while True:                                         # ponavljamo sledeći postupak
    n = int(input("Unesi prirodan broj: "))         # učitavamo naredni broj
    if n < 0:                                       # ako smo učitali -1, prekidamo izvrsavanje
        break
    if ima_parnih_cifara(n):                        # ako broj n sadrži bar jednu parnu cifru

        # ako je on prvi takav broj
        # ili je njegov zbir parnih cifara veći od prethodno najboljeg
        # ili je zbir jednak prethodno najboljem, ali je sam broj manji
        if (not postavljen_max or zbir_parnih_cifara(n) > zbir_parnih_cifara(max) or (zbir_parnih_cifara(n) == zbir_parnih_cifara(max) and n < max)):
            max = n                                 # ažuriramo najbolji broj
            postavljen_max = True                   # pronađen je broj sa parnom cifrom

# ispisujemo rezultat (-1 ako nije nađen nijedan broj sa parnim ciframa)
print("najmanji broj sa najvecim zbirom parnih cifara je ",max if postavljen_max else -1)
