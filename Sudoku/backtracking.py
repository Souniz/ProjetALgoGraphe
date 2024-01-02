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
def backtract(grapheMD:list,nb_couleur=0):
    """Colorier un graphe en utilisant l'algorithme de Glouton
    Args:
        graph ( type:GrapheMD): Un graphe de represente par une matrice d'adjecence
        nb_couleur(optionel):le nbre maximal de couleur 

    Returns:
        list: retourne une liste tel que la valeur de la ieme cas represente la couleur du sommet i
    """
    if(nb_couleur==0):
        nb_couleur=len(grapheMD)
    g=transform_en_listVoisin(grapheMD)
    sommet_couleur=[None for i in range(0,len(grapheMD))]
    couleur=[j for j in range(1,nb_couleur+1)]
    trouvCouleur(g,1,couleur,sommet_couleur)
    return sommet_couleur
def trouvCouleur(g,sommet,couleur,sommet_couleur):
    """Trouve la couleur d'un sommet par backtracking
    Args:
        voisin (list): les voisin du sommet a colorier
        couleur (list): la liste des couleurs
        sommet_couleur (list): liste telque la ieme case contient la couleur du sommet i ou
        None si le sommet n'est pas encore colorier

    Returns:
        int: la couleur choisit par backtracking
    """
    if(sommet==len(sommet_couleur)+1):
        return True
    non_valid=set(sommet_couleur[i-1] for i in g[sommet])
    for c in couleur:
        sommet_couleur[sommet-1]=c
        if c not in non_valid:
            if trouvCouleur(g,sommet+1,couleur,sommet_couleur):
                return True
    return False

