plik = open("pierwsze.txt").read().split()

pierwsze = []

for x in plik:
    pierwsza = False
    pierwsza2 = False
    z = x[::-1]
    x = int(x)
    z = int(z)
    for y in range(2, x//2):
        if x%y == 0:
            pierwsza = False
            break
        else:
            pierwsza = True
    for y in range(2, z//2):
        if z%y == 0:
            pierwsza2 = False
            break
        else:
            pierwsza2 = True
    if pierwsza and pierwsza2:
        pierwsze.append(x)

print(pierwsze)