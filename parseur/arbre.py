class Noeud:
    def __init__(self, term):
        self.valeur = term
        self.enfants = []

    def add(self, enfant):
        self.enfants.append(enfant)


class Arbre:
    def __init__(self, racine):
        self.racine = racine

    def print(self):
        self.print_rec(self.racine)

    def print_rec(self, noeud):
        print(noeud.valeur)
        for enfant in noeud.enfants:
            self.print_rec(enfant)
