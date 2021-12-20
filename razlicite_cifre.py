# Написати програм којим се испитује да ли су све цифре у декадном запису датог природног броја различите?
#
# Улаз: Са стандардног улаза уноси се природан број од 0 до 2 · 109.
#
# Излаз: На стандардном излазу исписује се текстуални одговор DA или NE.
#
# Пример 1
# Улаз
# 67569
# Излаз
# NE
# Пример 2
# Улаз
# 1234567890
# Излаз
# DA

# da li su sve cifre broja n različite
def razlicite_cifre(n):
    while n >= 10:                      # dok broj nije jednocifren
        if sadrzi_cifru(n//10, n%10):   # ako je poslednja cifra javlja
            # u delu broja ispred nje
            return False                # nisu sve cifre različite

        n //= 10                        # uklanjamo poslednju cifru
    return True                         # nijedna cifra se ne ponavlja

# provera da li dekadni zapis broja n sadrži datu cifru
def sadrzi_cifru(n, cifra):
    while True:                 # ponavljamo postupak
        if n % 10 == cifra:     # ako je poslednja cifra ona tražena
            return True         # broj sadrži cifru
        n = n // 10             # uklanjamo cifru
        if n == 0:              # ako je broj postao 0
            break               # prekidamo postupak
    return False                # cifra nije pronađena

n = int(input("Unesi prirodan broj: "))

# poziva funkciju iz komande za stampanje
print("DA" if razlicite_cifre(n) else "NE")
