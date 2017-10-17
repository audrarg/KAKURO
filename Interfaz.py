from Tkinter import *
from functools import partial
import Kakuro


class Application(Frame):
    Kakuro = Kakuro.Kakuro()
    matriz = []
    def ajustar(self,root,columnas,filas):
        width = 25 + 2 + (5 * columnas) + 2
        height = 2 + (2 * filas) + 2
        root.geometry("+%d+%d" % (width, height))


    def clean(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def __init__(self):
        root = Tk()
        root.configure(background='brown')
        root.geometry('600x500')
        root.title("Kakuro")
        Frame.__init__(self, root)
        self.pack()
        self.createWidgets(root)

    def crearKakuro(self, filas, columnas, panel,root):

        self.clean(panel)
        self.matriz = self.Kakuro.CrearKakuro(filas, columnas)
        rw = 20
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
                    columna.configure(text="(,"+str((matriz[m1][m2]) * -1)+')', bg="Maroon")

                clmn += 38
                m1 += 1
            rw += 42
            clmn = 10
            m1 = 0
            m2 += 1
        self.ajustar(root,columnas,filas)

    def createWidgets(self,root):

        m = PanedWindow(orient=HORIZONTAL)
        m.pack(fill=BOTH, expand=1)

        ##Panel Superior
        top = Label(m)
        top.configure(background="SaddleBrown")
        top.configure(width=25)
        m.add(top)

        btnSubir = Button(top, width=12, height=2, text="Cargar")
        btnSubir.configure(background="Peru")
        btnSubir.place(x=35, y=170)

        btnGuardar = Button(top, width=12, height=2, text="Guardar")
        btnGuardar.configure(background="Peru")
        btnGuardar.place(x=35, y=290)

        lblTam = Label(top, text="Seleccione el tamano del Kakuro", fg="white")
        lblTam.configure(background="SaddleBrown")
        lblTam.place(x=0, y=10)

        lblTam = Label(top, text="Cantidad de hilos", fg="white")
        lblTam.configure(background="SaddleBrown")
        lblTam.place(x=20, y=350)

        lblTam = Label(top, text="Cantidad de forks", fg="white")
        lblTam.configure(background="SaddleBrown")
        lblTam.place(x=20, y=400)

        lblHorz = Label(top, text="Horizontal", fg="white")
        lblHorz.configure(background="SaddleBrown")
        lblHorz.place(x=20, y=60)

        lblVert = Label(top, text="Vertical", fg="white")
        lblVert.configure(background="SaddleBrown")
        lblVert.place(x=20, y=100)

        spnHorz = Spinbox(top, from_=10, to=20, width=5)
        spnHorz.configure(background="Bisque")
        spnHorz.place(x=90, y=60)
        #spnHorz.configure(state = "readonly")

        spnVert = Spinbox(top, from_=10, to=20, width=5)
        spnVert.configure(background="Bisque")
        spnVert.place(x=90, y=100)
        #spnVert.configure(state="readonly")

        entryHilos = Entry(top)
        entryHilos.configure(background="Bisque")
        entryHilos.place(x=20, y=370)

        entryForks = Entry(top)
        entryForks.configure(background="Bisque")
        entryForks.place(x=20, y=420)

        ##Panel inferior
        bottom = Label(m)
        bottom.configure(background="BurlyWood")
        m.add(bottom)

        btnGenerar = Button(top, width=12, height=2, text="Generar",command=lambda: self.crearKakuro(int(spnHorz.get()), int(spnVert.get()), bottom, root))
        btnGenerar.configure(background="Peru")
        btnGenerar.place(x=35, y=230)
