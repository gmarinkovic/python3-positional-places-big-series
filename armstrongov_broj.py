# Написати програм који за дати природан број n проверава да ли је тај број Армстронгов. k-то цифрен број
# је Армстронгов ако је једнак суми k-тих степена својих цифара. На пример, 370 је Армстронгов јер је
# 370 = 3^3 + 7^3 + 0^3, 1634 је Армстронгов јер је 1634 = 1^4 + 6^4 + 3^4 + 4^4,
# док 12 није Армстронгов јер је 12  ̸= 1^2 + 2^2.
#
# Улаз: Са стандардног улаза се учитава природан број n (1 ≤ n ≤ 100000).
#
# Излаз: На стандардном излазу исписују се порука DA ако учитан број јесте Армстронгов, тј. NE ако учитан
# број није Армстронгов.
#
# Пример 1
# Улаз
# 1002
# Излаз
# NE
# Пример 2
# Улаз
# 370
# Излаз
# DA

# funkcija izracunava broj cifara broja n
def broj_cifara(n):
    broj = 0
    while True:
        broj = broj + 1
        n = n // 10
        if n == 0:
            break
    return broj

# funkcija izracunava zbir k-tih stepena cifara broja n
def zbir_ktih_stepena_cifara(n, k):
    zbir = 0
    while True:
        zbir = zbir + (n % 10) ** k
        n = n // 10
        if n == 0:
            break
    return zbir

# funkcija proverava da li je dati broj Armstrongov tj. ako broj ima k
# cifara, da li mu je zbir k-tih stepena cifara jednak njemu samom
def armstrongov(n):
    return zbir_ktih_stepena_cifara(n, broj_cifara(n)) == n

# ucitavamo broj i proveravamo da li je Armstrongov
n = int(input("Unesi prirodan broj: "))

print("Armstorngov broj:")
if armstrongov(n):
    print("DA")
else:
    print("NE")
