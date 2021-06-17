from tkinter import*
import random
import time;
import datetime




root = Tk()
root.geometry("1350x750+0+0")
root.title("vendas")
root.configure(background= 'blue')

Topo = Frame (root, width=1350 , height=100 , bd=8 ,relief ="raise")  # caixa do topo 
Topo.pack(side=TOP)

CaixaM = Frame (root, width=1000 , height=650 , bd=8 ,relief ="raise")   # caixa maior
CaixaM.pack(side=LEFT)  


caixa = Frame (root, width=450 , height=650 , bd=8 ,relief ="raise")  # caixa retangular 
caixa.pack(side=RIGHT)



lblInfo=Label(Topo,font=('arial',50,'bold'),text="MERCADINHO",bd=8,  width=33)  # TITULO 
lblInfo.grid(row=0,column=0)
              
# caixais segundarias 


  
root.mainloop()
