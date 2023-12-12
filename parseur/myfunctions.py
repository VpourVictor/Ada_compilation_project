from lexeur.file_to_code_ter import get_token


count = 0
list_token = get_token("name_file")

def fonction_N1(list_token): #N1 :284 285 A1 46 
    global count
    error = False
    if reader_carac(284, list_token[count],count) :
       
        if reader_carac(285, list_token[count], count) :
            if fonction_A1(list_token)[0] :
                count += fonction_A1[1]
                if reader_carac(285, list_token[count], count) :
                    return (True, count)
                else :
                    return (False, count)
            else :
                count += fonction_A1[1]
                return (False, count)
        else :
            return(False, count)
    else : 
        return(False, count)


    

def reader_carac(p1, p2, count):
    if p1 == p2:  # 284 = with
        count += 1
        return True
    elif compare([0][1], "with") < 2 :
       print("did you mean with, reçu : " + find_receive(list_token[count]))
       count += 1
       return True
    elif forgot_first_letter([0][1], "with")  :
       print("you forgot first letter " + find_receive(list_token[count]))
       count += 1
       return True
    else :
        print("attendu : with, reçu : " + find_receive(list_token[count]))
        return False
    
