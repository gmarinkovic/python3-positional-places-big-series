# Написати програм којим се испитује да ли декадни запис природног броја садржи дату цифру?
#
# Улаз: У првој линији стандардног улаза уноси се природан број од 0 до 1000000000, а у другој декадна
# цифра.
#
# Излаз: На стандардни излаз се исписује текстуални одговор, облика који је приказан у наредним примерима.
#
# Пример 1
# Улаз
# 29384
# 3
# Излаз
# broj 29384 sadrzi cifru 3
# Пример 2
# Улаз
# 29384
# 7
# Излаз
# broj 29384 ne sadrzi cifru 7

# !!!! kada zelimo da sacuvamo originalni broj a ne da ga celo vreme umanjujemo za jednu decimalnu poziciju !!!!
n = int(input("Unesi broj: "))
cifra = int(input("Unesi cifru koju trazis u zadatom broju: "))

m = n                           # kopiramo polaznu vrednost broja n
sadrzi = False                  # da li n sadrži cifru cifra

while True:                     # ponavljamo postupak
    if m % 10 == cifra:         # ako je poslednja cifra ona tražena
        sadrzi = True           # broj sadrži cifru
        break                   # prekidamo petlju
    m = m // 10                 # uklanjamo poslednju cifru
    if m == 0:                  # ako je broj m postao 0
        break                   # prekidamo postupak

print("broj ", n, " " if sadrzi else " ne ", "sadrzi cifru ", cifra, sep="")
