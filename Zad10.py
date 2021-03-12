from math import *

a = int(input())
try:
    print(a ** 0.5)  # w tym przypadku gdy a będize ujemne policzy pierwiastek ujemny
    print(pow(a, 0.5))  # w tym przypadku wyrzuci ValueError
    print(sqrt(a))  # w tym też
except ValueError as e:
    print(e)
