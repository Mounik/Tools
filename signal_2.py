import signal
import os
import time

def alarme(signal, contexte):
    print("Réception du signal no %s " % signal )
    raise OSError("Alarme !!!")

MAX_TIME = 5 # en secondes

signal.signal(signal.SIGALRM, alarme)
signal.alarm(MAX_TIME)

print("Début du temps d'attente ...")
try:
    time.sleep(15)
except:
    pass

# sinon on continue
print("Fin du temps d'attente ...")

signal.alarm(0)
