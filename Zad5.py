import sys as system

system.stdout.write("Podaj trzy liczby całkowite: ")
a = int(system.stdin.readline())
b = int(system.stdin.readline())
c = int(system.stdin.readline())

system.stdout.write(str(a**b+c))
