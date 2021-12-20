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

# provera da li dekadni zapis broja n sadrži datu cifru
def sadrzi_cifru(n, cifra):
    while True:                 # ponavljamo postupak
        if n % 10 == cifra:     # ako je poslednja cifra ona tražena
            return True         # broj sadrži cifru
        n = n // 10             # uklanjamo cifru
        if n == 0:              # ako je broj postao 0
            break               # prekidamo postupak
    return False            # cifra nije pronađena

n = int(input("Unesi broj: "))
cifra = int(input("Unesi cifru koju trazis u zadatom broju: "))

# u printu pokrece funkciju sadrzi_cifru
print("broj ", n, " " if sadrzi_cifru(n, cifra) else " ne ", "sadrzi cifru " , cifra, sep="")
