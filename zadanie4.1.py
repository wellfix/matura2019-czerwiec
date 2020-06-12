plik = open("liczby.txt").read().split()

pierwsze = []

for x in plik:
    pierwsza = False
    x = int(x)
    if x < 100 or x > 5000:
        continue
    for y in range(2, x//2):
        if x%y == 0:
            pierwsza = False
            break
        else:
            pierwsza = True
    if pierwsza:
        pierwsze.append(x)

print(pierwsze)


