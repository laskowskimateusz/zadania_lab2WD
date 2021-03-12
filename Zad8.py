n=0
lista = []

while n<10:
    liczba = int(input())
    if liczba % 2 == 0:
        lista.append(liczba)
    n += 1
print(lista)
