# Природан број се трансформише тако што се замени производом својих цифара. Написати програм којим се
# исписују све трансформације броја док се не добије једноцифрен број. Одредити и колико трансформација
# је при томе потребно извршити.
#
# Улаз: Једна линија стандардног улаза садржи један природан број.
#
# Излаз: На стандардном излазу приказати у свакој линији по једну трансформацију датог броја (природан
# број), до једноцифреног броја. У последњој линији стандардног излаза приказати број трансформација.
#
# Пример 1
# Улаз
# 3274
# Излаз
# 168
# 48
# 32
# 6
# 4

# Пример 2
# Улаз
# 5
# Излаз
# 0

# računa proizvod cifara broja n
def proizvod_cifara(n):
    p = 1                   # proizvod cifara
    while True:             # ponavljamo postupak
        p = p * (n % 10)    # množimo proizvod poslednjom cifrom broja
        n = n // 10         # uklanjamo poslednju cifru broja n
        if n == 0:          # kada broj dostigne 0
            break           # prekidamo postupak
    return p                # vraćamo izračunati proizvod


n = int(input("Unesi prirodan broj: "))         # broj koji analiziramo
brojac = 0                                      # broj transformacija dok ne postane jednocifren
while n >= 10:                                  # dok je broj visecifren
    n = proizvod_cifara(n)                      # menjamo ga proizvodom njegovih cifara
    print(n)                                    # ispisujemo promenjeni broj
    brojac = brojac + 1                         # uvecavamo broj transformacija

print(brojac, "transformacije")
