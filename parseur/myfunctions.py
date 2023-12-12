from lexeur.file_to_code_ter import get_token

count_tmp = 0 #
count = 0
list_token = get_token("name_file")

def fonction_ (list_token):
    global count
    global count_tmp

def fonction_N16(): #N16 ::= 34 A16 34
    global count
    global count_tmp
    local_ind = 0
    if reader_carac(34) :
        if fonction_A16():
            if reader_carac(34) :
    return False

def fonction_A16(): #A16 ::= N12 | N13 | 44 | 58 | 40 | 41 | 45 | 61 | 60 | 62 | 43 | 42 | 47 | 46 | 95 | 34
    global count
    global count_tmp
    if reader_carac(34) :
        return True
    elif reader_carac()





    

def reader_carac(p1):
    #traiter le cas ou p2 est un couple
    global count
    global count_tmp
    if p1 == token_list[count_tmp]:  # 284 = with
        count_tmp += 1
        return True
    elif compare(token_list[count_tmp][1], 284) :
       print("did you mean with, reçu : " + find_receive(list_token[count]))
       count_tmp += 1
       return True
    elif forgot_first_letter(p1, "with")  :
       print("you forgot first letter " + find_receive(list_token[count]))
       count_tmp += 1
       return True
    else :
        print("attendu : with, reçu : " + find_receive(list_token[count]))
        return False
    
def test_is_correct(p1, str) :

    #relier les cas au dictionnaire

    def compare(p,str):

        return False
    
    def forgot_a_letter(p,str):

        return False
    
    return (True)