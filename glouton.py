def transform_en_listVoisin(graphMD):
    """Transforme un graphe de matrice d'adjecence en 
       dictionnaire dont chaque sommet est associe à une liste representant ces voisin

    Args:
        graphMD (list): Matrice d'adjecence
    Returns:
        dic: dictionnaire represent les voisin de chaque sommet
    """
    diction={}
    for i in range(0,len(graphMD)):
         l=[]
         for j in range(0,len(graphMD[i])):
           if graphMD[i][j]:
               l.append(j+1)
         diction[i+1]=l  
    return diction
#------------------------------------------------
def trie_sommet(grapheTL:dict):
    """Retourne une liste des sommets trier par leur degre

    Args:
        graphe (dict):type dictionnaire
    """
    s=[i for i in range(1,len(grapheTL)+1)]
    for i in range(0,len(s)):
        for j in range(0,len(s)):
            if len(grapheTL[i+1])>len(grapheTL[j+1]):
                tmp=s[i]
                s[i]=s[j]
                s[j]=tmp
    return s
#------------------------------------------------
def coloriage_glouton(graph:list,nb_couleur=0):
    """Colorier un graphe en utilisant l'algorithme de Glouton
    Args:
        graph ( type:GrapheMD): Un graphe de represente par une matrice d'adjecence

        Returns:
        list: retourne une liste tel que la valeur de la ieme cas represente la couleur du sommet i
    """
    if(nb_couleur==0):
        nb_couleur=len(graph)
    listvoisin=transform_en_listVoisin(graph)
    sommets=trie_sommet(listvoisin)
    color=[i for i in range(1,nb_couleur+1)]
    sommet_color=[None for i in range(0,len(graph))]
    for sommet in sommets:
        color_no_valid=set(sommet_color[i-1] for i in listvoisin[sommet])
        sommet_color[sommet-1]=min([i for i in color if i not in color_no_valid])
    return sommet_color

a=[[0,1,1,0,0,1,0,0,0],
      [1,0,1,1,0,0,1,0,0],
      [1,1,0,1,1,0,0,0,0],
      [0,1,1,0,1,0,1,1,0],
      [0,0,1,1,0,1,0,0,0],
      [1,0,0,0,1,0,0,1,1],
      [0,1,0,1,0,0,0,0,0],
      [0,0,0,1,0,1,0,0,1],
      [0,0,0,0,0,1,0,1,0]]
# print()

# import time
# start_time = time.time()
# coloriage_glouton(a)
# print("--- %s seconds ---" % (time.time() - start_time))
print(coloriage_glouton(a))





        

