from datetime import *
from dateutil.relativedelta import *

## Aujourd'hui
today = datetime.now()

# Date de sortie de la première version de python
python_v1 = datetime(1991, 2, 20, 12, 00, 00)

## Calcul du nombre de jours depuis avec datetime
print( 'datetime today - python_v1 : ', today - python_v1)

# calcul avec dateutil
print( 'dateutil today - python_v1 : ', relativedelta(today, python_v1))

# dateutil permet de rajouter des mois et des années
print("relative delta : ajout de 1 an + 1 mois : ",
today+relativedelta(years=+1, months=+1))

# et même de soustraire
print("relative delta : retrait de 1 an : ", today+relativedelta(years=-1))