def calculDegre(G:list,s:int):
    """Calcule le degre du  sommet (s)

    Args:
        G (list): Matrice d'adjecence
        s (sommet): le sommet qu'on calcule son degre

    Returns:
        int: le degre du sommet
    """
    degre=0
    for i in range(0,len(G)):
        if G[s][i]:
            degre=degre+1
    return degre
#-------------------------------------------
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
def trie_sommet(grapheMD:list):
    """Retourne une liste des sommets trier par leur degre

    Args:
        graphe (dict):type dictionnaire
    """
    s=[i for i in range(1,len(grapheMD)+1)]
    for i in range(0,len(s)):
        for j in range(0,len(s)):
            if calculDegre(grapheMD,s[i]-1)>calculDegre(grapheMD,s[j]-1):
                tmp=s[i]
                s[i]=s[j]
                s[j]=tmp
    return s
#---------------------------------------------------
def trouveColor(voisin:list,Sommet_color:list,color:list):
    """Retourne la plus petite couleur disponible sans creer de conflit

    Args:
        voisin (list): liste des voisins 
        Sommet_color (list): tableau des sommets des colories
        color (list): liste des couleurs

    Returns:
        int: la plust petite couleur disponible
    """
    color_no_valid=set(Sommet_color[i-1] for i in voisin)
    return min([i for i in color if i not in color_no_valid])

#------------------------------------------------
def coloriage_glouton(graph:list):
    """Colorier un graphe en utilisant l'algorithme de Glouton
    Args:
        graph ( type:GrapheMD): Un graphe de represente par une matrice d'adjecence

        Returns:
        list: retourne une liste tel que la valeur de la ieme cas represente la couleur du sommet i
    """
    sommets=trie_sommet(graph)
    color=[i for i in range(1,len(graph)+1)]
    listvoisin=transform_en_listVoisin(graph)
    sommet_color=[None for i in range(0,len(graph))]
    for sommet in sommets:
        sommet_color[sommet-1]=trouveColor(listvoisin[sommet],sommet_color,color)
    return sommet_color

a=[[0,1,0],
       [1,0,1],
       [0,1,0]]
print(coloriage_glouton(a))





        

