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
import time
import numpy as np
graphe= np.array([[0,0,0,1,1,0,0,1,0],
                  [1,0,0,1,1,0,0,1,0], 
                  [1,0,0,0,0,0,0,1,0], 
                  [0,0,1,0,1,1,0,1,0],
                  [0,1,1,0,0,1,0,0,0],
                  [1,0,1,0,1,0,0,1,0],
                  [1,0,0,0,0,0,0,1,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,1,1,0,1,0,0,1,0]])
start_time = time.time()
print(degré(graphe))
print(algo_powell(graphe))
print("--- %s seconds ---" % (time.time() - start_time))


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
start_time = time.time()
graphe= np.array([[0,0,0,1,1,0,0,1,0],
                  [1,0,0,1,1,0,0,1,0], 
                  [1,0,0,0,0,0,0,1,0], 
                  [0,0,1,0,1,1,0,1,0],
                  [0,1,1,0,0,1,0,0,0],
                  [1,0,1,0,1,0,0,1,0],
                  [1,0,0,0,0,0,0,1,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,1,1,0,1,0,0,1,0]])
print(glouton(graphe))
print("--- %s seconds ---" % (time.time() - start_time))