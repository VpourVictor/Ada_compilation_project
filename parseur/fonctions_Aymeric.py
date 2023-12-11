from arbre import Noeud
import pdb

def fonction_N2(list_index):
    return (False, 2)

def fonction_A1(list_index):
    if list_index == []:
        return (True,0)
    save = fonction_N2(list_index)
    save2 = fonction_A1(list_index[save[1]:])

    if save[0]:
        if save2[0]:
            return (True,save[1] + save2[1])
        return (False, save[1] + save2[1])
    else:
        return(False, save[1])
    

