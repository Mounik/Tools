from path import Path
from subprocess import check_output

d = Path(".")

total = 0
for fic in sorted(d.files("*.odt")):
    cmd = "odt2txt %s | wc -m" % fic
    nb_car=check_output(cmd, shell=True, text=True, universal_newlines=True)

    total += int(nb_car)

    print("%-70s : %15s" (fic, nb_car.strip()))

# Affichage du total
print("%88s" % ("-" * 15))
print("%70s : %15s" % ("Total", total))
