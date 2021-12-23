# Написати програм којим се исписује k децимала бинарног записа реаланог броја x (0 ≤ x < 1) .
#
# Улаз: Прва линија стандардног улаза садржи реалан број из интервала [0,1). Друга линија стандардног улаза
# садржи природни број k (1 ≤ k ≤ 100).
#
# Излаз: У првој и јединој линији стандардног излаза приказати бинарни запис броја x, заокружен на k децимала.
# Пример
# Улаз
# 0.8
# 4
# Излаз
# 0.1100

x = float(input("Unesi realna broj u rasponu od 0 do 1 : "))
k = int(input("Unesi broj decimala: "))

print("0,", end="")

for i in range(k):
    x = x * 2
    print(int(x), end="")
    x = x - int(x)
