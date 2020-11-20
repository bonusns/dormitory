kolvo_detaley = []

chislo_rabocih = 10
max = 100000000000000000000

while chislo_rabocih > 0:
    detal = int(input("Сколько деталей ты сделал? "))
    kolvo_detaley.append(detal)
    chislo_rabocih = chislo_rabocih - 1

chislo_rabocih = 10

for nomer_rabochigo in range(0,chislo_rabocih):
    if kolvo_detaley[nomer_rabochigo] >= 1000:
        print(f"Рабочий под номером {nomer_rabochigo+1} получает зп")
        if 1001 <= kolvo_detaley[nomer_rabochigo] <= 1500:
            print("Премия +1000\n")
        elif 1501 <= kolvo_detaley[nomer_rabochigo] <= max:
            print("Премия +2000\n")
        else:
            print()
    else:
        print(f"Дядя под номером {nomer_rabochigo+1} ты в этом месяце без зп\n")
