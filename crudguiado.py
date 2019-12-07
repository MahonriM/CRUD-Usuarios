from tkinter import *
from tkinter import messagebox
import sqlite3
#---funciones--------

def conexionBBDD():
    miConexion= sqlite3.connect("Usuarios")
    micursor=miConexion.cursor()
    try:
        micursor.execute(''' 
           Create Table DATOSUSUARIOS(ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),PASSWORD VARCHAR(50),APELLIDO VARCHAR(10),
           DIRECCION VARCHAR(50),COMENTARIO VARCHAR(100))''')
        messagebox.showinfo("BBDD", "BBDD creada con exito")
    except:
        messagebox.showwarning("¡ATENCION!","La BBDD ya existe")
def Saliraplicacion():
    valor=messagebox.askquestion("Salir","¿Deseas salir?")
    if valor=="yes":
        root.destroy()
def limpiarcampos():
    miID.set("")
    miNombre.set("")
    miDireccion.set("")
    miapellido.set("")
    miPass.set("")
    textoComentari.delete(1.0,END)
def crear():
    miConexion=sqlite3.connect("Usuarios")
    micursor = miConexion.cursor()
    micursor.execute("Insert Into  DATOSUSUARIOS VALUES(NULL,'"+ miNombre.get()+"','"+miPass.get()+"','"+miapellido.get()+"','"
                     +miDireccion.get()+"','"+textoComentari.get("1.0",END)+"')")
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro insertado con exito")
def leer():
    miConexion=sqlite3.connect("Usuarios")
    micursor = miConexion.cursor()
    micursor.execute("Select * FROM DATOSUSUARIOS WHERE ID="+miID.get())
    elusuario=micursor.fetchall()
    for usuario in elusuario:
        miID.set(usuario[0])
        miNombre.set(usuario[1])
        miPass.set(usuario[2])
        miapellido.set(usuario[3])
        miDireccion.set(usuario[4])
        textoComentari.insert(1.0,usuario[5])
        miConexion.commit()
def crear2():
    try:
        miConexion = sqlite3.connect("Usuarios")
        micursor = miConexion.cursor()
        micursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?, ?, ?,?,?)", (
        miNombre.get(), miPass.get(), miapellido.get(), miDireccion.get(), textoComentari.get("1.0", END)))
        miConexion.commit()
        messagebox.showinfo("BBDD", "Registro insertado con exito")
    except:
        messagebox.showinfo("BBDD","Algo a fallado")
def actualizar():
    try:
        miConexion= sqlite3.connect("Usuarios")
        micursor=miConexion.cursor()
        micursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?,PASSWORD=?,APELLIDO=?,DIRECCION=? ,COMENTARIO=? WHERE ID=?",
                         (
                             miNombre.get(), miPass.get(), miapellido.get(), miDireccion.get(),
                             textoComentari.get("1.0", END),miID.get()
                         ))
        miConexion.commit()
        messagebox.showinfo("BBDD","Registro actualizado")
    except:
        messagebox.showinfo("BBDD","Algo a fallado")
def eliminar():
    try:
        miConexion=sqlite3.connect("Usuarios")
        micursor=miConexion.cursor()
        micursor.execute("Delete From DATOSUSUARIOS WHERE ID=?",(miID.get()))
        miConexion.commit()
        messagebox.showinfo("BBDD","Registro Eliminado")
    except:
        messagebox.showinfo("BBDD","Algo a fallado")
root = Tk()
barramenu=Menu(root)
root.config(menu=barramenu,width=300,height=300)
bbddMenu=Menu(barramenu,tearoff=0)
bbddMenu.add_command(label="Conectar",command=conexionBBDD)
bbddMenu.add_command(label="Salir",command=Saliraplicacion)

borrarMenu=Menu(barramenu,tearoff=0)
borrarMenu.add_command(label="Borrar campos",command=limpiarcampos)

crudMenu=Menu(barramenu,tearoff=0)
crudMenu.add_command(label="Crear",command=crear)
crudMenu.add_command(label="Leer",command=leer)
crudMenu.add_command(label="Acutializar",command=actualizar)
crudMenu.add_command(label="Eliminar",command=eliminar)

ayudaMenu=Menu(barramenu,tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de ..")

barramenu.add_cascade(label="BBDD",menu=bbddMenu)
barramenu.add_cascade(label="Borrar",menu=borrarMenu)
barramenu.add_cascade(label="Crud",menu=crudMenu)
barramenu.add_cascade(label="Ayuda",menu=ayudaMenu)
#----Comienzo de campos de label y textbox
miFrame=Frame(root)
miFrame.pack()

miID=StringVar()
miNombre=StringVar()
miapellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

CuadroID=Entry(miFrame,textvariable=miID)
CuadroID.grid(row=0,column=1,padx=10,pady=10)

CuadroNombre=Entry(miFrame,textvariable=miNombre)
CuadroNombre.grid(row=1,column=1,padx=10,pady=10)
CuadroNombre.config(fg="red",justify="right")

Cuadropass=Entry(miFrame,textvariable=miPass)
Cuadropass.grid(row=2,column=1,padx=10,pady=10)
Cuadropass.config(show="?")

CuadroApellido=Entry(miFrame,textvariable=miapellido)
CuadroApellido.grid(row=3,column=1,padx=10,pady=10)

CuadroDireccion=Entry(miFrame,textvariable=miDireccion)
CuadroDireccion.grid(row=4,column=1,padx=10,pady=10)

textoComentari=Text(miFrame,width=16,height=5)
textoComentari.grid(row=5,column=1,padx=10,pady=10)

scrollvelt=Scrollbar(miFrame,command=textoComentari.yview)
scrollvelt.grid(row=5,column=2,sticky="nsew")
textoComentari.config(yscrollcommand=scrollvelt.set)
#--Aqui van los labels
idlabel=Label(miFrame,text="Id:")
idlabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

Nombrelabel=Label(miFrame,text="Nombre:")
Nombrelabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

passlabel=Label(miFrame,text="Password:")
passlabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)


Apellidolabel=Label(miFrame,text="Apellido:")
Apellidolabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

direccionlabel=Label(miFrame,text="Direccion:")
direccionlabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

comentarioslabel=Label(miFrame,text="Comentarios:")
comentarioslabel.grid(row=5,column=0,sticky="e",padx=10,pady=10)
#-----------------Aqui van los botones--------------------------
miFrame2=Frame(root)
miFrame2.pack()
botonCrear=Button(miFrame2,text="Crear",command=crear)
botonCrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)

botonLeer=Button(miFrame2,text="Read",command=leer)
botonLeer.grid(row=1,column=1,sticky="e",padx=10,pady=10)


botonActualizar=Button(miFrame2,text="Update",command=actualizar)
botonActualizar.grid(row=1,column=2,sticky="e",padx=10,pady=10)

botonBorrar=Button(miFrame2,text="Delete",command=eliminar)
botonBorrar.grid(row=1,column=3,sticky="e",padx=10,pady=10)


root.mainloop()

