
import random

peso = 0
peso0a10= 0
peso10a20 = 0
peso20a30= 0
pesoMasDe30 = 0


for i in range(0,300):
    peso = random.randint(0,45)

    if peso > 0 and peso < 10:
        peso0a10 += 1

    elif peso > 10 and peso < 20:
        peso10a20 += 1

    elif peso > 20 and peso < 30:
        peso20a30 += 1

    elif peso > 30:
        pesoMasDe30 += 1

print(peso0a10,peso10a20,peso20a30,pesoMasDe30)