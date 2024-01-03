from tkinter import*
import numpy as np
from sommet import Sommet
from backtracking import backtract
from tkinter.messagebox import showerror
class Sudoku(Tk):
    def __init__(self):
        super().__init__()
        self.sommets=np.array([[Sommet((i,j)) for j in range(0,9)] for i in range(0,9)])
        self.case= [[Entry(self,width=5) for i in range(0,9)] for j in range(0,9)]
        self.jouer=Button(self,text='Solution',command=self.colorier,bg='green',width=20,foreground='white')
        self.rejouer=Button(self,text='Recommencer',command=self.recommencer,bg='blue',width=20,foreground='white')
        self.sommet_color=0
        self.createCase()
        self.jouer.grid(row=11,column=2,columnspan=4,pady=(10,0))
        self.rejouer.grid(row=12,column=2,columnspan=4,pady=(10,0))
        self.ajoutEvenKey()
        self.geometry('480x400')
        self.mis_en_forme()
        self.recupVoisin()
        self.configure(pady=50,padx=9)
    def createCase(self):
        """Creation de la grile de Sudoku
        """
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
    def ajoutEvenKey(self):
        """Controler le saisie
        """
        for i in range(0,9):
            for j in range(0,9):
                self.case[i][j].bind('<KeyRelease>',self.suprimCaract)
    def colorier(self):
         """Fonction coloriage
         """
         self.sommet_color=[i.get() if i.get()!='' else 0 for i in np.array(self.case).reshape(81,)]
         sommet=self.sommets.copy()
         sommet=sommet.reshape(81,)
         graphMD=np.zeros((81,81))
         for i in range(len(sommet)):
            for j in range(len(sommet)):
                if sommet[j] in sommet[i].voisins:
                     graphMD[i][j]=1
         if(backtract(graphMD,self.sommet_color,9)):
            self.sommet_color=np.array(self.sommet_color)
            self.sommet_color=self.sommet_color.reshape((9,9))
            for i in range(0,9):
                for j in range(0,9):
                    if self.case[i][j].get() =='':
                        self.case[i][j]['bg']='#E9967A'
                    self.case[i][j].delete("0")
                    self.case[i][j].insert("0",self.sommet_color[i][j])
         else:
             print('Pas de solution')
             showerror("Errer","Pas de Solution")
    def mis_en_forme(self):
        for i in range(0,9):
            for j in range(0,9):
                self.case[i][j].config(font=5,justify=CENTER)
    def recommencer(self):
        """Jouer une autre partie
        """
        self.sommet_color=0
        for i in range(0,9):
            for j in range(0,9):
                self.case[i][j]['bg']='white'
                self.case[i][j].config(font=5,justify=CENTER)
                self.case[i][j].delete("0")
    def recupVoisin_lign_colon(self):
        """Recupere les voisin sur la ligne et sur la colone 
        """
        for i in range(0,9):
            for j in range(0,9):
                l=set(self.sommets[i:i+1,:].reshape(9,)) #voison par ligne
                c=set(self.sommets[:,j:j+1].reshape(9,)) #voisin par colone
                vois=l.union(c) 
                self.sommets[i][j].voisins=vois
                self.sommets[i][j].supprim_self() # Supprime le sommet lui meme
    def recupVoisin(self):
        """Recupe les voisin sur la carre et les fusionner
          avec les voisins sur la ligne et sur la colone deja recuperer
        """
        self.recupVoisin_lign_colon() #Pour recuperer les voisin de ligne et de colone
        for i in range(0,9,3): #Je fais des saut de 3 pour recuperer le premier element de chaque carre
            for j in range(0,9,3):
                 voi_car=set(self.sommets[i:i+3,j:j+3].reshape(9,)) #Recuperation des voisin carree
                 for k in range(3):      #Rcuperation des voisin des autres sommet de meme carre
                     for l in range(3):
                         self.sommets[i+k][j+l].voisins=self.sommets[i+k][j+l].voisins.union(voi_car)
                         self.sommets[i+k][j+l].supprim_self() 
    def suprimCaract(self,event:Event):
       if event.widget.get() <'1' or event.widget.get()>'9' or len(event.widget.get())>1:
             event.widget.delete("0",'end')
#-------------------------------------------------------------              
if __name__=='__main__':
    sudoku= Sudoku()
    sudoku['bg']='#008B8B'
    sudoku.title('Suduko')
    sudoku.mainloop()
    
