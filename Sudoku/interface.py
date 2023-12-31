from tkinter import*
class Sudoku(Tk):
    
    def __init__(self):
        super().__init__()
        self.case= [[Entry(self,width=5) for i in range(0,9)] for j in range(0,9)]
        self.jouer=Button(self,text='Solution',command=self.colorier,bg='green',width=20,foreground='white')
        self.title('Sudoku')
        self.createCase()
        self.jouer.grid(row=11,column=2,columnspan=4,pady=(10,0))
        self.geometry('400x250')

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
if __name__=='__main__':
    sudoku= Sudoku()
    sudoku['bg']='gray'
    sudoku.mainloop()
