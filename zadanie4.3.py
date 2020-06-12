def W(x):
    x = list(x)
    for z in range(len(x)):
        x[z] = int(x[z])
    return str(sum(x))


plik = open("pierwsze.txt").read().split()
licznik = 0
for x in plik:
    while int(x) >= 10:
        x = W(x)
    if int(x) == 1:
        licznik += 1

print(licznik)
