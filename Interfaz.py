from Tkinter import *
from functools import partial
import Kakuro


class Application(Frame):

    Kakuro = Kakuro.Kakuro()

    def clean(self,frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def __init__(self):
        root = Tk()
        root.configure(background='brown')
        root.minsize(width=800, height=630)
        root.maxsize(width=800, height=630)
        Frame.__init__(self, root)
        self.pack()
        self.createWidgets()


    def crearKakuro(self, filas, columnas, panel):

        self.clean(panel)
        matriz = self.Kakuro.CrearKakuro(filas, columnas)
        rw = 200
        clmn = 10
        m1 = 0
        m2 = 0
        for i in range(0, filas):
            for j in range(0, columnas):
                columna = Label(panel, text=str(matriz[m1][m2]), height=1, width=2, relief="solid")
                columna.place(x=rw, y=clmn)
                if matriz[m1][m2] == -1:
                    columna.configure(background="Black")

                elif matriz[m1][m2] < 0:
                    columna.configure(text=str((matriz[m1][m2]) * -1), fg="Maroon")

                clmn += 22
                m1 += 1
            rw += 21
            clmn = 10
            m1 = 0
            m2 += 1


    def createWidgets(self):

        m = PanedWindow(orient=VERTICAL)
        m.pack(fill=BOTH, expand=1)

        ##Panel Superior
        top = Label(m)
        top.configure(background="SaddleBrown")
        top.configure(height=10)
        m.add(top)

        btnSubir = Button(top, width=12, height=2, text="Subir")
        btnSubir.configure(background="Peru")
        btnSubir.place(x=200, y=100)

        btnGuardar = Button(top, width=12, height=2, text="Guardar")
        btnGuardar.configure(background="Peru")
        btnGuardar.place(x=440, y=100)

        lblTam = Label(top, text="Seleccione el tamano del Kakuro", fg="white")
        lblTam.configure(background="SaddleBrown")
        lblTam.place(x=80, y=10)

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

        spnHorz = Spinbox(top, from_=10, to=20, width=5)
        spnHorz.configure(background="Bisque")
        spnHorz.place(x=125, y=40)
        ##spnHorz.pack()

        spnVert = Spinbox(top, from_=10, to=20, width=5)
        spnVert.configure(background="Bisque")
        spnVert.place(x=235, y=40)
        ##spnVert.pack()

        ##Panel inferior
        bottom = Label(m)
        bottom.configure(background="BurlyWood")
        m.add(bottom)

        btnGenerar = Button(top, width=12, height=2, text="Generar", command= lambda : self.crearKakuro(int(spnHorz.get()),int(spnVert.get()),bottom))
        btnGenerar.configure(background="Peru")
        btnGenerar.place(x=320, y=100)



