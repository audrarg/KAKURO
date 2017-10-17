from Tkinter import *
from functools import partial
import Kakuro


class Application(Frame):
    Kakuro = Kakuro.Kakuro()

    def clean(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def __init__(self):
        root = Tk()
        root.configure(background='brown')
        root.minsize(width=1205, height=950)
        root.maxsize(width=1205, height=950)
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
        for i in range(0, columnas):
            for j in range(0, filas):
                columna = Label(panel, text=str(matriz[m1][m2]), height=2, width=5, relief="solid")
                columna.place(x=rw, y=clmn)
                if matriz[m1][m2] == -1:
                    columna.configure(background="Black")

                elif matriz[m1][m2] < 0:
                    columna.configure(text="(,"+str((matriz[m1][m2]) * -1)+')', fg="Maroon")

                clmn += 38
                m1 += 1
            rw += 42
            clmn = 10
            m1 = 0
            m2 += 1

    def createWidgets(self):

        m = PanedWindow(orient=VERTICAL)
        m.pack(fill=BOTH, expand=1)

        ##Panel Superior
        top = Label(m)
        top.configure(background="SaddleBrown")
        top.configure(height=8)
        m.add(top)

        btnSubir = Button(top, width=12, height=2, text="Subir")
        btnSubir.configure(background="Peru")
        btnSubir.place(x=400, y=80)

        btnGuardar = Button(top, width=12, height=2, text="Guardar")
        btnGuardar.configure(background="Peru")
        btnGuardar.place(x=640, y=80)

        lblTam = Label(top, text="Seleccione el tamano del Kakuro", fg="white")
        lblTam.configure(background="SaddleBrown")
        lblTam.place(x=350, y=10)

        lblTam = Label(top, text="Cantidad de hilos", fg="white")
        lblTam.configure(background="SaddleBrown")
        lblTam.place(x=660, y=10)

        lblTam = Label(top, text="Cantidad de forks", fg="white")
        lblTam.configure(background="SaddleBrown")
        lblTam.place(x=660, y=40)

        lblHorz = Label(top, text="Horizontal", fg="white")
        lblHorz.configure(background="SaddleBrown")
        lblHorz.place(x=340, y=40)

        lblVert = Label(top, text="Vertical", fg="white")
        lblVert.configure(background="SaddleBrown")
        lblVert.place(x=455, y=40)

        spnHorz = Spinbox(top, from_=10, to=20, width=5)
        spnHorz.configure(background="Bisque")
        spnHorz.place(x=400, y=40)


        spnVert = Spinbox(top, from_=10, to=20, width=5)
        spnVert.configure(background="Bisque")
        spnVert.place(x=500, y=40)

        entryHilos = Entry(top)
        entryHilos.configure(background="Bisque")
        entryHilos.place(x=770, y=10)

        entryForks = Entry(top)
        entryForks.configure(background="Bisque")
        entryForks.place(x=770, y=40)

        ##Panel inferior
        bottom = Label(m)
        bottom.configure(background="BurlyWood")
        m.add(bottom)

        btnGenerar = Button(top, width=12, height=2, text="Generar",command=lambda: self.crearKakuro(int(spnHorz.get()), int(spnVert.get()), bottom))
        btnGenerar.configure(background="Peru")
        btnGenerar.place(x=520, y=80)
