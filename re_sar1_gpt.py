import re
from pathlib import Path
import matplotlib.pyplot as plt

# Répertoire de base des fichiers sar
dir_base = "/var/log/sysstat/"  # Peut être différent selon les distributions
data = {}

STORE = False

# Récupération des données
for f in Path(dir_base).glob("*.sar"):
    with open(f) as fic:
        lines = fic.readlines()
        for line in lines:
            d = re.findall(r"\S+", line)  # Divise la ligne en mots
            if "%idle" in d:  # Début des données intéressantes
                STORE = True
                continue
            if "Moyenne" in d:  # Fin des données intéressantes
                STORE = False
                continue
            if STORE and "all" in d:
                try:
                    t = d[0]  # Heure ou timestamp
                    pcu = 100 - float(d[-1].replace(",", "."))  # %idle -> %CPU utilisé
                    file_key = f.name  # Nom du fichier actuel
                    if file_key in data:
                        data[file_key][0].append(t)
                        data[file_key][1].append(pcu)
                    else:
                        data[file_key] = [[t], [pcu]]
                except (ValueError, IndexError) as e:
                    print(f"Erreur lors du traitement de la ligne : {line}")
                    print(f"Exception : {e}")
                    continue

# Vérification si `data` contient des données
if not data:
    print("Aucune donnée trouvée dans les fichiers sar.")
else:
    # Affichage graphique
    first_key = list(data.keys())[0]  # Récupérer la première clé
    x = data[first_key][0]  # Timestamps
    y = data[first_key][1]  # %CPU utilisé
    plt.plot(x, y)
    # Suppression des libellés sur l'axe X car illisibles
    plt.xticks([], [])
    plt.title(f"Utilisation CPU depuis le fichier {first_key}")
    plt.ylabel("Utilisation CPU (%)")
    plt.xlabel("Temps")
    plt.grid(True)
    plt.show()
