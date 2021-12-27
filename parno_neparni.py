# Пера се игра картама. Све карте које је имао у руци је сложио тако да прво иду све карте са парним бројевима,
# а затим оне са непарним бројевима (могуће је и да је Пера имао само парне или само непарне карте). Напиши
# програм који проверава да ли је Пера исправно сложио карте.
#
# Улаз: Са стандардног улаза учитавају се бројеви карата (природни бројеви између 2 и 10) све док се не дође
# до краја улаза (он се може унети са Ctrl+Z тј. Ctrl+D). Карата има најмање две, а највише десет.
#
# Излаз: На стандардни излаз исписати da ако је Пера добро сложио карте тј. ne у супротном.
#
# Пример 1
# Улаз
# 2
# 6
# 4
# 5
# 3
# Излаз
# da
#
# Пример 2
# Улаз
# 2
# 6
# 3
# 5
# 4
# Излаз
# ne
import sys

OK = True                   # da li je serija za sada ispravna
neparni = False             # da li smo u presli u deo sa neparnim brojevima

for linija in sys.stdin:    # čitamo jedan po jedan broj sa ulaza, prekid sa CTRL+D
    x = int(linija)
    if x % 2 != 0:          # ako je broj neparan,
        neparni = True      # prelazimo na čitanje neparnih brojeva
    else:
        if neparni:         # paran se broj javio u neparnom delu niza
            OK = False      # konstatujemo grešku i prekidamo petlju
            break

print("da" if OK else "ne") # ispisujemo rezultat
