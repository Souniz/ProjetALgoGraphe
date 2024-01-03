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
def pre_verification(g,some_coul):
    """Verifie qu'on a pas saisie des chiffre qui respect
      pas la regle du jeu de suduko

    Args:
        g (dict): le graphe de dictionaire
        some_coul (list): les chiffre(couleur) deja saisi(attribuer)

    Returns:
        bool: True si c'est bon 
    """
    for sommet in g:
        non_valid=set(int(some_coul[i-1]) for i in g[sommet])
        if some_coul[sommet-1]!= 0 and int(some_coul[sommet-1]) in non_valid:
            return False
    return True
def backtract(grapheMD:list,sommet_couleur,nb_couleur=0):
    """Colorier un graphe en utilisant l'algorithme de Glouton
    Args:
        graph ( type:GrapheMD): Un graphe de represente par une matrice d'adjecence
        sommet_couleur(type:n):liste dont l'element a l'indice i represente la couleur 
        du sommet i+1 et vide('') si le sommet n'a pas encore de couleur
        nb_couleur(type:n)(optionel):le nbre maximal de couleur 

    Returns:
        list: retourne une liste tel que la valeur de la ieme cas represente la couleur du sommet i
    """
    if(nb_couleur==0):
        nb_couleur=len(grapheMD)
    g=transform_en_listVoisin(grapheMD)
    if not pre_verification(g,sommet_couleur):
        return False
    return trouvCouleur(g,1,nb_couleur,sommet_couleur)
def trouvCouleur(g,sommet,nb_couleur,sommet_couleur):
    """Trouve la couleur d'un sommet par backtracking
    Args:
        graph ( type:dictionnaire): Un graphe de represente un dictionnaire dont chaque sommet est
        associe a sa liste de succeseur 
        nb_couleur (int): nombre de couleur de couleurs
        voisin (list): le premier sommet a colorier
        sommet_couleur (list): liste telque la ieme case contient la couleur du sommet i ou
        0 si le sommet n'a pas encore de couleur
        """
    if(sommet==len(sommet_couleur)+1):
        return True
    non_valid=set(int(sommet_couleur[i-1]) for i in g[sommet])
    if type(sommet_couleur[sommet-1])==str:
        if trouvCouleur(g,sommet+1,nb_couleur,sommet_couleur):
          return True
        return False
    for c in range(1,nb_couleur+1):
        sommet_couleur[sommet-1]=c
        if c not in non_valid:
            if trouvCouleur(g,sommet+1,nb_couleur,sommet_couleur):
                return True
    sommet_couleur[sommet-1]=0
    return False

