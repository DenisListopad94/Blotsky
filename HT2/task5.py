# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

imie = "Ivanou Ivan"
s = imie.split()
s.reverse()

result = " ".join(s)

print(result)
