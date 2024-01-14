import lexeur.file_to_code_ter as file
import parseur.functions
import lexeur.dictionnaire_ter as dictionnaire_ter

if __name__ == '__main__':
    # token_list = file.get_token("exemples/intro.ada")
    # print(token_list)
    # print(parseur.functions.fonction_N1(token_list))
    print(dictionnaire_ter.term)
    # token_list = file.get_token("exemples/exemple_calcul.ada") # -> fonctionne
    # token_list = file.get_token("exemples/exemple.ada")
    token_list = file.get_token("exemples/exemple_petite_procedure.ada") # -> fonctionne
    # token_list = file.get_token("exemples/exemple_procedure.ada")
    print(token_list)
    print(parseur.functions.fonction_N1(token_list))
