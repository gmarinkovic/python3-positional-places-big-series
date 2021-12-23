# Одреди првих k децималних цифара вредности 1/n за дати позитиван природан број n. Претпоставити да се
# након k децимала врши одсецање тј. да се број заокружује наниже.
#
# Улаз: Прва линија стандардног улаза садржи природан број k (1 ≤ k ≤ 1000) а друга природан број n
# (2 ≤ n ≤ 1000).
#
# Излаз: На стандардном излазу, приказујемо количник са траженим бројем децимала
# (потребно је употребити децималну запету, а не децималну тачку).

# Пример
# Улаз
# 4
# 33
# Излаз
# 0,0303

# broj decimala
k = int(input("Unesi broj decimala koji zelimo da se pojave: "))

# imenilac
n = int(input("Unesi prirodan broj koji je delilac: "))

print("Kolicnik sa trazenim brojem decimala: ","0,", end="")
broj = 1 # tekući deljenik

for i in range(k):
    print((10 * broj) // n, end="")     # određujemo narednu cifru
    broj = (10 * broj) % n              # ažuriramo deljenik
