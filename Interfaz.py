import pickle
from Tkinter import *
import tkFileDialog
import Kakuro
import time
import threading


class Application(Frame):
    Kakuro = Kakuro.Kakuro()
    matriz = []

    def load(self,filename):
        file = open(filename, "rb")
        matriz2 = pickle.load(file)
        file.close()
        return matriz2


    def save(self,filename, archivo):
        file = open(filename, "wb")
        pickle.dump(archivo, file)
        file.close()
        print "Archivo guardado"

    def nombre(self,filas,columnas):
        archivo = "Kakuro" + str(filas) + "x" + str(columnas) + time.strftime("%H-%M-%S") + ".p"
        return archivo

    def clean(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()



    def __init__(self):
        root = Tk()
        root.configure(background='brown')
        root.geometry('1920x1080')
        root.title("Kakuro")
        Frame.__init__(self, root)
        self.pack()
        self.createWidgets(root)

    def kakuro(self,filas,columnas):
        kakuro = Kakuro.Kakuro()
        kakuro.CrearKakuro(filas,columnas)

    def crearKakuro(self, filas, columnas, panel):

        '''
        for i in range(9,30):
            self.Kakuro.CrearKakuro(i, i)
        '''
        self.clean(panel)
        self.matriz = self.Kakuro.CrearKakuro(filas, columnas)
        rw = 20
        clmn = 10
        m1 = 0
        m2 = 0
        for i in range(0, columnas):
            for j in range(0, filas):
                columna = Label(panel, text=str(self.matriz[m1][m2]), height=2, width=5, relief="solid")
                columna.place(x=rw, y=clmn)
                if self.matriz[m1][m2] == -1:
                    columna.configure(background="Black")

                elif isinstance(self.matriz[m1][m2],int) == False:
                    if len(self.matriz[m1][m2]) > 1:
                        columna.configure(text=str((self.matriz[m1][m2][0]))+'\\'+str((self.matriz[m1][m2][1])*-1) , bg="Maroon")
                    else:
                        columna.configure(text=str((self.matriz[m1][m2][0]))+'\\',bg="Maroon")


                elif self.matriz[m1][m2] < 0:
                    columna.configure(text='\\'+str((self.matriz[m1][m2]) * -1), bg="Maroon")

                clmn += 38
                m1 += 1
            rw += 42
            clmn = 10
            m1 = 0
            m2 += 1


    def abrirKakuro(self, matrizKakuro, panel):

        self.clean(panel)
        rw = 20
        clmn = 10
        m1 = 0
        m2 = 0
        for i in range(0, len(matrizKakuro[0])):
            for j in range(0, len(matrizKakuro)):
                columna = Label(panel, text=str(matrizKakuro[m1][m2]), height=2, width=5, relief="solid")
                columna.place(x=rw, y=clmn)
                if matrizKakuro[m1][m2] == -1:
                    columna.configure(background="Black")

                elif matrizKakuro[m1][m2] < 0:
                    columna.configure(text="(," + str((matrizKakuro[m1][m2]) * -1) + ')', bg="Maroon")

                clmn += 38
                m1 += 1
            rw += 42
            clmn = 10
            m1 = 0
            m2 += 1

    def abrirArchivo(self,root,panel):
        root.filename = tkFileDialog.askopenfilename(initialdir="C:\Users\Audra\KAKURO", title="Select file",filetypes=(("jpeg files", "*.p"), ("all files", "*.*")))
        self.abrirKakuro(self.load(root.filename),panel)

    def guardarArchivo(self):
        filename = self.nombre(len(self.matriz),len(self.matriz[0]))
        self.save(filename, self.matriz)
        print filename

    def createWidgets(self,root):

        m = PanedWindow(orient=HORIZONTAL)
        m.pack(fill=BOTH, expand=1)

        ##Panel Superior
        top = Label(m)
        top.configure(background="SaddleBrown")
        top.configure(width=25)
        m.add(top)



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

        btnGenerar = Button(top, width=12, height=2, text="Generar",command=lambda: self.crearKakuro(int(spnHorz.get()), int(spnVert.get()), bottom))
        btnGenerar.configure(background="Peru")
        btnGenerar.place(x=35, y=230)

        btnSubir = Button(top, width=12, height=2, text="Cargar", command = lambda: self.abrirArchivo(root,bottom))
        btnSubir.configure(background="Peru")
        btnSubir.place(x=35, y=170)

        btnGuardar = Button(top, width=12, height=2, text="Guardar", command = self.guardarArchivo)
        btnGuardar.configure(background="Peru")
        btnGuardar.place(x=35, y=290)
