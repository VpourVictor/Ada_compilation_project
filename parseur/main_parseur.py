import lexeur.file_to_code_ter as file
import parseur.functions

if __name__ == '__main__':
    token_list = file.get_token("exemples/intro.ada")
    print(token_list)
    print(parseur.functions.fonction_N1(token_list))


