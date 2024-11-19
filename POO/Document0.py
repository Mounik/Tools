from datetime import datetime

class Document:
    def __init__(self, titre="Titre du document", auteur="Lui" ):
        self.titre = titre
        self.auteur = auteur
        self.date_creation = datetime.now(). strftime("%d/%m/%Y à %H : %M : %S")
        self.contenu = None

    def __str__(self):
        t = """
Titre : %s

%s

Créé le : %s par %s

        """ % (self.titre, self.contenu,
                        self.date_creation, self.auteur )
        return t

    def __repr__(self):
        return "<Document : %s  : %d >" % (self.titre, id(self))

if __name__ == '__main__':
    D = Document( "Titre", "Moi")
    D.contenu = """
Bonjour,
je suis le contenu de ce document
et je dois être imprimé comme tel
    """
    print(D)