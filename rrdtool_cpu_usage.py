import rrdtool
import time
import datetime
import random

FICHIER="fichier.rrd"


def get_temps():
    return int(datetime.datetime.now().strftime("%s"))
# la date en seconde

timing = get_temps()

debut=timing #on stocke le debut

rrdtool.create(
    FICHIER,
    "--start", "%s" % debut,
    "--step", "600",
    "DS:cpu_usage:GAUGE:600:0:100",
    "RRA:AVERAGE:0.5:1:288",
    )

for t in range(0, 6 * 12): # 600 secondes * 6 = 1h * 12 = 12h

    R = random.randint(0, 100)
    timing += 600
    if t in (2,12,18):
        R = random.randint(5, 19)
    if t in (5,10,15):
        R = random.randint(105, 120)
    rrdtool.update(FICHIER, "%s:%03d" % (timing, R))

fin=timing #on stocke la fin

print ( "debut : ", time.strftime('%d-%m-%Y %H:%M:%S',
time.localtime(debut)) , debut)
print ( "Fin   : ", time.strftime('%d-%m-%Y %H:%M:%S',
time.localtime(fin)) , fin)

result = rrdtool.graph("cpu_usage.png",
                        '--start', "%i" % debut,
                        '--end', "%i" % fin,
                        '--title', 'CPU USAGE',
                        'DEF:fichier=%s:cpu_usage:AVERAGE' % FICHIER,
                        'LINE1:fichier#FF0000:CPU_USAGE',
                        'HRULE:80#0000FF:"Limite Haute"',
                        'HRULE:20#00FF00:"Limite Basse"'
                        )