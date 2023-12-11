import lexeur.dictionnaire_ter as dictionnaire_ter

class Term:
    def __init__(self, token, string):
        self.token = token
        self.string = string

    def __str__(self):
        return str(self.token) + ' : ' + self.string

    def create_term(self, token, string):
        return Term(token, string)

    def assign(self):
        list_term = []
        for string, token in dictionnaire_ter.term.items():
            list_term.append(self.create_term(token, string))

        return list_term
