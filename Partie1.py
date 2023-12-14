#COLORIAGE DE GRAPHES

#Implantatio en Phyton trois algorithmes qui permettent de colorier un graphe
#: glouton, Welsh-Powell et backtracking. Vous trouverez sur le net, plusieurs
#documents et vidéos sur cet argument.

#%% Algorithme de Welsh-Powell
#définition du degré de chaque sommet et le trier de manière décroissante
def degré(graphe):
    Nb_suc={}
    for i in range(0,len(graphe)):
        L=[]
        for j in range(0,len(graphe)):
            if graphe[i,j]==1:
                L.append(j)
                Nb_suc[i]=len(L)
    #Trie de Nb_suc
    Nb_suc = dict(sorted(Nb_suc.items(), key=lambda item: item[1],reverse=True))

    return Nb_suc

#Algorithme de Powell  

def algo_powell(graphe):
    Nb_suc=degré(graphe)
    powel={}
    color=0
    for s in Nb_suc.keys():
        if s not in powel:
            powel[s]=color
            for v in range(len(graphe)):
                if graphe[s,v]==0 and v not in powel: #je cherche les non-voisins de s qui ne sont pas coloriés
                    powel[v]=color
            color=color+1
    powel=dict(sorted(powel.items(), key=lambda item: item[1]))

    return powel


    
#test
import numpy as np
graphe= np.array([[0,0,0,1,1],[1,0,0,1,1], [1,0,0,0,0], [0,0,1,0,0],[0,0,1,0,0]])
print(degré(graphe))
print(algo_powell(graphe))


# %% Algorithme de glouton
import numpy as np
def glouton(graphe):
    glouton={}
    color=0
    for s in range(len(graphe)):
        if s not in glouton:
            glouton[s]=color
            for v in range(len(graphe)):
                if graphe[s,v]==0 and v  not in glouton: #je cherche les non-voisins de s qui ne sont pas coloriés
                    if graphe[v,s]==0:
                        glouton[v]=color
            color=color+1
    glouton=dict(sorted(glouton.items(), key=lambda item: item[1]))
    return glouton
#test
graphe= np.array([[0,0,0,1,1],[1,0,0,1,1], [1,0,0,0,0], [0,0,1,0,0],[0,0,1,0,0]])
print(glouton(graphe))

#%% Algorithme de Backtracking
#Fonction qui vérifie que deus sommets adjacents n'ont pas la même couleur
def color_valide(graphe,s,colors,color):
    for v in range(len(graphe)):
        if colors[s]==color and colors[v]==color:
            return False,v
        return True,v

def backtracking(graphe,colors,Nb_colors):
    colors=np.zeros((Nb_colors,Nb_colors),dtype=int)
    if colors!=0:
        return True
    for s in range(len(graphe)):
        for c in range(1,Nb_colors):
            test_color=color_valide(graphe,s,colors,c)
            if test_color[0]==True:
                v=test_color[1]
                colors[s,v]=c
                if backtracking(graphe,colors,Nb_colors):
                    return True
                colors[s,v]=c+1
    return False

#test
def colorier(gaphe):
graphe= np.array([[0,0,0,1,1],[1,0,0,1,1], [1,0,0,0,0], [0,0,1,0,0],[0,0,1,0,0]])
print(glouton(graphe))



    
            