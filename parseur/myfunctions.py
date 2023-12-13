from lexeur.file_to_code_ter import get_token


count = 0
count_tmp = 0
list_token = get_token("name_file")

def fonction_N1(): #N1 :284 285 A1 46 
    global count
    global list_token

    if reader_carac(284, list_token[count]) :
        if reader_carac(285, list_token[count]) :
            if fonction_A1(list_token)[0] :
                count += fonction_A1[1]
                if reader_carac(285, list_token[count]) :
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


    

def reader_carac(token_attendu):
    if p1 == p2:  # 284 = with
        count += 1
        return True
    elif compare(p1, p2) < 2 :
       print("did you mean with, reçu : " )
       count += 1
       return True
    else :
        print("attendu : with, reçu : ")
        return False
    
