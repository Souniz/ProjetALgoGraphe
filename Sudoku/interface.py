from tkinter import*
import numpy as np
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
        self.voisins.remove(self)
class Sudoku(Tk):
    
    def __init__(self):
        super().__init__()
        self.sommets=np.array([[Sommet((i,j)) for j in range(0,9)] for i in range(0,9)])
        self.case= [[Entry(self,width=5) for i in range(0,9)] for j in range(0,9)]
        self.jouer=Button(self,text='Solution',command=self.colorier,bg='green',width=20,foreground='white')
        self.title('Sudoku')
        self.createCase()
        self.jouer.grid(row=11,column=2,columnspan=4,pady=(10,0))
        self.geometry('400x250')
        self.recupVoisin_carre()

    def createCase(self):
        for i in range(0,9):
            for j in range(0,9):
               if (j==2 and i==2) or (j==5 and i==2) or (j==2 and i==5) or (j==5 and i==5) :
                   self.case[i][j].grid(row=i,column=j,padx=(0, 5),pady=(0, 5))
               elif (j==2 or j==5):
                    self.case[i][j].grid(row=i,column=j,padx=(0, 5))
               elif  i==2 or i==5: 
                   self.case[i][j].grid(row=i,column=j,pady=(0, 5))
               else:
                   self.case[i][j].grid(row=i,column=j,padx=(0, 0),pady=(0, 0))
    def colorier(self):
         sommet=[]
         for i in range(0,9):
            for j in range(0,9):
                sommet.append(self.case[i][j].get())
         print(sommet)
    def recupVoisin_lign_colon(self):
        for i in range(0,9):
            for j in range(0,9):
                l=set(self.sommets[i:i+1,:].reshape(9,)) #voison par ligne
                c=set(self.sommets[:,j:j+1].reshape(9,)) #voisin par colone
                vois=l.union(c) 
                self.sommets[i][j].voisins=vois
                self.sommets[i][j].supprim_self() # Supprime le sommet lui meme
    def recupVoisin_carre(self):
        self.recupVoisin_lign_colon() #Pour recuperer les voisin de ligne et de colone
        for i in range(0,9,3):
            for j in range(0,9,3):
                 voi_car=set(self.sommets[i:i+3,j:j+3].reshape(9,))
                 for k in range(3):
                     for l in range(3):
                         self.sommets[i+k][j+l].voisins=self.sommets[i+k][j+l].voisins.union(voi_car)
                         self.sommets[i+k][j+l].supprim_self() 
        print(list(self.sommets[0][0].voisins)[18].coord)   
if __name__=='__main__':
    sudoku= Sudoku()
    sudoku['bg']='gray'

    sudoku.mainloop()
    
