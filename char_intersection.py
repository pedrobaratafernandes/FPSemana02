# input O r a n g o t a n g o s
# input O r n i t o r r i n c o
# output nOort

#ora = "Orangotangos"
#teste = "Ornitorrinco"
ora = input()
teste = input()

palavra1 = set()
palavra2 = set()
final = set()
for letra in ora:
    palavra1.add(letra)

for letra in teste:
    palavra2.add(letra)

for letra in palavra1:
    if letra in palavra2:
        final.add(letra)
x = ""

for palavra in final:
    x +=palavra
y = ""
for palavra in sorted(x, key=str.lower):
    y += palavra

print(y)
