# Написати програм који у датом природном броју свако појављивање цифре 0 замењује цифром 5.
#
# Улаз: Са стандардног улаза се учитава природан број у границама од 0 до 1000000000.
#
# Излаз: На стандардном излазу се исписује добијени број.
#
# Пример
# Улаз
# 20240607
# Излаз
# 25245657

# u broju n zamenjuje svako pojavljivanje cifre a, cifrom b
def zameni(n, a, b):
    t = 1 # težina naredne cifre (1, 10, 100, ...)
    novi_broj = 0 # broj koji se dobija nakon zamene
    # prolazimo kroz sve cifre broja n, sdesna nalevo
    while True:
        c = n % 10 # izdvajamo cifru jedinica
        n = n // 10 # uklanjamo cifru jedinica iz broja n
        # u novi broj, na početak upisujemo:
        # - cifru b, ako je c == a,
        # - cifru c, inače
        novi_broj = novi_broj + (b if c == a else c) * t
        t = t * 10 # izračunavamo težinu naredne cifre
        if n == 0:
            break
    return novi_broj # vraćamo novoformirani broj

# ucitavamo broj i menjamo sve nule peticama
n = int(input("Unesi prirodan broj: "))
print("Novi broj je : ",zameni(n, 0, 5))
