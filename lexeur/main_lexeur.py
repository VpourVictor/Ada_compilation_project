import lexeur.file_to_code_ter as file

if __name__ == '__main__':
    print("On commence les tests par un hello world :")
    print(file.get_token("exemples/hello.ada"))
    print(
        "On voit que l'ensemble des tokens sont reconnus. Sauf les caractères \" qui ne sont pas dans le dictionnaire")

    print("Ce second exemple montre que les erreurs sont bien reconnues :")
    print(file.get_token("exemples/exemple_erreur.ada"))
    print("Les caractères spéciaux ne sont pas dans le dictionnaire, donc ils ne sont pas reconnus")
    print("On affiche bien les numéros de lignes qui posent problème")

    print("Le prochain exemple illuste la reconnaissance des mots clés intervenant dans un code avec des if :")
    print(file.get_token("exemples/exemple_if.ada"))
    print("On voit bien que les mots clés sont reconnus")

    print("On teste maintenant la reconnaissance des numéros :")
    print(file.get_token("exemples/exemple_num.ada"))
    print("On remarque que les numéros sont bien reconnus, et ce quelque soit le placement des espaces")
    print("Il n'y a aucune distinction entre 5+3 et 5 + 3")

    print("Enfin on teste notre lexeur sur un code plus complexe :")
    print(file.get_token("exemples/exemple.ada"))
    print("On remarque que les mots clés sont bien reconnus")
    print("On remarque que les numéros sont bien reconnus")
    print("On remarque que les identificateurs sont bien reconnus (unDebut, aireRectangle, larg et long, etc.)")
