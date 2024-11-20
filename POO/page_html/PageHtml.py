import Document # Je dois importer le module Document

## La classe PageHtml avec Document.Document (module.classe)
## comme classe parente
class PageHtml(Document.Document):
    def __init__(self, titre="Page HTML"):
        super().__init__(titre)  ## __init__ de la classe parente
        self.contenu = []        ## je force contenu en liste vide

    def head(self):
        return """
            <head>
                <title> %s </title>
            </head>\n
            """ % self.titre

    def body(self):
        return """
            <body>
            %s
            </body>\n
            """ % self.retourne_contenu()

    def footer(self):
        return """
            <footer> Crée par %s le %s </footer>\n
            """ % ( self.auteur, self.date_creation)

    def __str__(self):
        t = """
            <html>
            %s
            %s
            %s
            </html>
        """ %  ( self.head(), self.body(), self.footer() )
        return t

    def __repr__(self):
        return "<PageHtml : %s  : %d >" % (self.titre, id(self))

if __name__ == "__main__":
    P = PageHtml()
    P.titre = "Page HTML"
    P.contenu.append( " <p> Bonjour le monde </p>" )
    print(P)