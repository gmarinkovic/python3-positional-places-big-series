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

# vraća zbir parnih cifara broja ako broj n sadrži bar jednu parnu
# cifru, a vrednost -1 ako broj n ne sadrži parnu cifru
def zbir_parnih_cifara(n):
    ima_parnih_cifara = False           # da li broj sadrzi parnu cifru?
    zbir = 0                            # zbir parnih cifara

    while True:
        if n % 2 == 0:                  # skraćeno od (n % 10) % 2 == 0
            ima_parnih_cifara = True    # pronađena je parna cifra
            zbir = zbir + n % 10        # uvećavamo zbir
        n = n // 10                     # uklanjamo cifru
        if n == 0:                      # ako je broj postao 0
            break                       # prekidamo postupak

    # vraćamo ili izračunati zbir ili -1 ako parna cifra nije nađena
    return zbir if ima_parnih_cifara else -1


max = -1                                        # najbolji do sada pročitani broj
                                                # -1 ukazuje da do sada nije bilo brojeva sa parnim ciframa
zbir_parnih_cifara_max =-1

while True:                                     # ponavljamo sledeći postupak
    n = int(input("Unesi prirodni broj: "))     # učitavamo naredni broj
    if n == -1:                                 # ako smo učitali -1, prekidamo izvršavanje
        break
    # izračunavamo zbir parnih cifara broja n
    zbir_parnih_cifara_n = zbir_parnih_cifara(n)
    if zbir_parnih_cifara_n != -1:              # ako broj n sadrzi parnu cifru
        # ako je on prvi takav broj
        # ili je njegov zbir parnih cifara veci od prethodno najboljeg
        # ili je jednak prethodno najboljem, ali je sam broj manji
        if max == -1 or zbir_parnih_cifara_n > zbir_parnih_cifara_max or zbir_parnih_cifara_n == zbir_parnih_cifara_max and n < max:
            # ažuriramo najbolji broj i njegov zbir cifara
            max = n
            zbir_parnih_cifara_max = zbir_parnih_cifara_n

print("Najmanji broj sa maksimalnim zbirom parnih cifara je", max)
