# fichier : matplotlib1.py

import matplotlib.pyplot as plt
import random

data = [ random.randint(5, 25) for x in range(0,20) ]

plt.title(" Données Aléatoires")     # le titre
plt.plot(data)                       # transmission des données
plt.ylabel('Label axe des Y')        # titre de l'axe Y
plt.xlabel('Label axe des X')        # titre de l'axe X
plt.show()                           # Affichage