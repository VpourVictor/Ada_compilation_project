from arbre import Noeud
import pdb
from myfunctions import *

def fonction_A1(): #A1 ::= '' A1 ::= N2 A1
    global count
    global count_tmp
    count_tmp = count
    global list_token

    if fonction_N2():
        if fonction_A1():
            count = count_tmp
            return True
        
        count_tmp = count
        return False
    
    count_tmp = count
    return True
    
def fonction_A3(): #A3 ::= '' A3 ::= 285
    global count
    global count_tmp
    count_tmp = count
    global list_token

    if reader_carac(285):
        count = count_tmp
        return True
    
    count_tmp = count
    return False    

    

def fonction_N2 (): #N2 ::= 281 285 N21 
    #N2 ::= A5 58 N4 A6 59 
    #N2 ::= 274 285 A7 267 A1 258 A2 261 A3 59 
    #N2 ::= 264 285 A7 277 N4 267 A1 258 A2 261 A3 59

    global count
    global count_tmp
    count_tmp = count
    global list_token

    if reader_carac(281):
        if reader_carac(285):
            if fonction_N21():
                count=count_tmp
                return True

    count_tmp = count

    if fonction_A5():
        if reader_carac(58):
            if fonction_N4():
                if fonction_A6():
                    if reader_carac(59):
                        count=count_tmp
                        return True
                        
    count_tmp = count
    
    if reader_carac(274):
        if reader_carac(285):
            if fonction_A7():
                if reader_carac(267):
                    if fonction_A1():
                        if reader_carac(258):
                            if fonction_A2():
                                if reader_carac(261):
                                    if fonction_A3():
                                        if reader_carac(59):
                                            count=count_tmp
                                            return True

    count_tmp = count

    if reader_carac(264):
        if reader_carac(285):
            if fonction_A7():
                if reader_carac(277):
                    if fonction_N4():
                        if reader_carac(267):
                            if fonction_A1():
                                if reader_carac(258):
                                    if fonction_A2():
                                        if reader_carac(261):
                                            if fonction_A3():
                                                if reader_carac(59):
                                                    count=count_tmp
                                                    return True
    count_tmp = count                                      
    return False

def fonction_N21(): #N21 ::= 59
                    #N21 ::= 267 N22

    global count
    global count_tmp
    count_tmp = count
    global list_token

    if reader_carac(59):
        count = count_tmp
        return True
    
    count=count_tmp

    if reader_carac(267):
        if fonction_N22():
            count = count_tmp
            return True
        
    count_tmp = count
    return False

def fonction_N22(): #N22 ::= 256 285 59
                    #N22 ::= 275 A4 261 275 59


    global count
    global count_tmp
    count_tmp = count
    global list_token

    if reader_carac(256):
        if reader_carac(285):
            if reader_carac(59):
                count = count_tmp
                return True
    
    count_tmp = count

    if reader_carac(275):
        if fonction_A4():
            if reader_carac(261):
                if reader_carac(275):
                    if reader_carac(59):
                        count = count_tmp
                        return True
    
    count_tmp = count
    return False


def fonction_A4():#A4 ::= N3 A42
    global count
    global count_tmp
    count_tmp = count
    global list_token

    if fonction_N3():
        if fonction_A42():
            count = count_tmp
            return True
        
    count_tmp = count
    return False


def fonction_A42():#A42 ::= '' A42 ::=  A4
    global count
    global count_tmp
    count_tmp = count
    global list_token

    if fonction_A4():
        count = count_tmp
        return True
    
    count_tmp = count
    return True

def fonction_A5():#A5 ::= 285 A52
    global count
    global count_tmp
    count_tmp = count
    global list_token

    if reader_carac(285):
        if fonction_A52():
            count = count_tmp
            return True
        
    count_tmp = count
    return False

def fonction_A52():
#A52 ::= ''
#A52 ::= 44 A5
    global count
    global count_tmp
    count_tmp = count
    global list_token

    if reader_carac(44):
        if fonction_A5():
            count = count_tmp
            return True
    
    count_tmp = count
    return True

def fonction_A6():
#A6 ::= ''
#A6 ::= 58 61 N8
    global count
    global count_tmp
    count_tmp = count
    global list_token

    if reader_carac(58):
        if reader_carac(61):
            if fonction_N8():
                count = count_tmp
                return True
            
    count_tmp = count
    return False

def fonction_A7():
#A7 ::= '' 
#A7 ::= N5
    global count
    global count_tmp
    count_tmp = count
    global list_token

    if fonction_A5():
        count = count_tmp
        return True
    
    count_tmp = count
    return True


def fonction_N3():
#N3 ::= A5 58 N4 59
    pass