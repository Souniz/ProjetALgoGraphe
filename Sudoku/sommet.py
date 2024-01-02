class Sommet:
    def __init__(self,coord) -> None:
        self.coord=coord
        self.couleur=0
        self.voisins=set()
    def __eq__(self, other: object) -> bool:
        if self.coord[0]==other.coord[0] and self.coord[1]==other.coord[1]:
            return True
        else:
            return False
    def __hash__(self) -> int:
        return self.coord[0]+self.coord[1]
    def supprim_self(self):
        """Permet de supprimer le sommet lui sur la liste des voisins
        """
        self.voisins.remove(self)