import json
import random

with open("prueba.json") as file:
    dex = json.load(file)

length = len(dex)
chosenNro = random.randint(1,length)

print("Recibiste un",dex[chosenNro],". ¡Cuídalo bien! ♥")
