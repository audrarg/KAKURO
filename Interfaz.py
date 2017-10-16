from Tkinter import *
from functools import partial

class Application(Frame):
    def printS(self,spinbox,spinbox2):
        stri = spinbox.get(), "HORIZONTAL", spinbox2.get(), "VERTICAL"
        print stri


    def crearKakuro(self, filas, columnas, matriz,panel):

        rw = 200
        clmn = 10
        m1 = 0
        m2 = 0
        for i in range(0,filas):
            for j in range(0,columnas):
                columna = Label(panel, text= str(matriz[m1][m2]), height=1, width=2,relief="solid")
                columna.place(x=rw, y=clmn)
                if matriz[m1][m2] == -1:
                    columna.configure(background="Black")

                elif matriz[m1][m2] < 0:
                    columna.configure(text = str((matriz[m1][m2])*-1), fg = "Maroon")

                clmn += 22
                m1 +=1
            rw +=21
            clmn = 10
            m1 = 0
            m2 += 1

    def createWidgets(self):


         matriz = [[-1, -1, -1, -1,-1, -1, -1, -1, -1, -1],
                 [-1, -5, 2, 3, -1, -1, -6, 1, 5, -1],
                 [-1 ,-1 ,-1 ,-1 ,-9 ,2 ,7 ,-6, 1, 5],
                 [-1 ,-1 ,-1, -1, -1, -18, 2, 8 ,7, 1],
                 [-1 ,-1 ,-1 ,-1 ,-17 ,6 ,4 ,7, -1 ,-1],
                 [-1, -1, -1, -1, -1, -1, -1, -7, 2, 5],
                 [-1 ,-1 ,-1, -24 ,3, 5, 6, 2, 7, 1],
                 [-20, 3 ,6 ,1 ,2 ,8 ,-19, 9, 6, 4],
                 [-1 ,-1, -1, -1 ,-1 ,-1 ,-11, 7, 4 ,-1],
                 [-1 ,-1 ,-15, 7 ,8 ,-25, 9, 8, 1, 7]]

         m = PanedWindow(orient=VERTICAL)
         m.pack(fill=BOTH, expand=1)

         ##Panel Superior
         top = Label(m)
         top.configure( background = "SaddleBrown" )
         top.configure( height = 10)
         m.add(top)

         btnSubir = Button(top, width=12, height=2, text = "Subir")
         btnSubir.configure(background="Peru")
         btnSubir.place(x=200, y=100)

         btnGuardar = Button(top, width=12, height=2, text="Guardar")
         btnGuardar.configure(background="Peru")
         btnGuardar.place(x=440, y=100)

         lblTam = Label(top, text="Seleccione el tamano del Kakuro", fg = "white")
         lblTam.configure(background="SaddleBrown")
         lblTam.place(x = 80, y = 10)

         lblTam = Label(top, text="Cantidad de hilos", fg="white")
         lblTam.configure(background="SaddleBrown")
         lblTam.place(x=400, y=10)

         lblTam = Label(top, text="Cantidad de forks", fg="white")
         lblTam.configure(background="SaddleBrown")
         lblTam.place(x=400, y=40)

         lblHorz = Label(top, text="Horizontal", fg="white")
         lblHorz.configure(background="SaddleBrown")
         lblHorz.place(x=60, y=40)

         lblVert = Label(top, text="Vertical", fg="white")
         lblVert.configure(background="SaddleBrown")
         lblVert.place(x=190, y=40)

         spnHorz = Spinbox(top, from_ = 10, to = 20, width = 5)
         spnHorz.configure(background="Bisque")
         spnHorz.place(x = 125, y = 40)

         spnVert = Spinbox(top, from_=10, to=20, width=5)
         spnVert.configure(background="Bisque")
         spnVert.place(x=235, y=40)

         ##Panel inferior
         bottom = Label(m)
         bottom.configure(background="BurlyWood")
         m.add(bottom)

         parametros = partial(self.crearKakuro, int(spnHorz.get()),int(spnVert.get()),matriz,bottom)
         btnGenerar = Button(top, width=12, height=2, text="Generar", command = parametros)
         btnGenerar.configure(background="Peru")
         btnGenerar.place(x=320, y=100)


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
root.configure(background='brown')
root.minsize(width=800, height=600)
root.maxsize(width=800, height=600)
app = Application(master=root)
app.mainloop()
root.destroy()

