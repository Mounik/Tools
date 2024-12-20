import multiprocessing as mp
import random
import time

# Définition d'un canal de communication
output = mp.Queue()

# Fonction exemple avec temps d'attente
# + génération de nombres aléatoires
def fonction(temps, output):
    time.sleep(temps)
    data = [ random.randint(0,100) for x in range(1,1000) ]
    total = sum(data)
    output.put(total)

# Création d'une liste de processus
processes = [mp.Process(target=fonction, args=(5, output)) for x
in range(4)]

# Lancement des processus
for p in processes:
    p.start()

# Fermeture des processus
for p in processes:
    p.join()

# Récupération des données
results = [output.get() for p in processes]

print(results)