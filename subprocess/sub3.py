import subprocess
import time

def do_requete(commande, requete):
    cmd = subprocess.Popen(commande, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    output, error = cmd.communicate(input=requete)
    if error:
        print("STDERR : %s " % error)
    return output


USER="userdev"            # l'utilisateur de la base de données
MPD="xxxxxxxx"            # son mot de passe
SERVEUR="localhost"       # le serveur
DATABASE="basedev"        # la base de données

## la commande "mysql"
commande = [
       "mysql",
       "--user="+USER,
       "--password="+MPD,
       "--host="+SERVEUR,
       "--database="+DATABASE
       ]

## une requete simple
requete = "select count(*) from villes_france_free;\n"
r = do_requete(commande, requete)
print("output :\n %s" % r)

## une autre requete simple
requete = """select count(*) from villes_france_free
            where
            ville_departement='01';\n"""
r = do_requete(commande, requete)
print("output :\n %s" % r)
