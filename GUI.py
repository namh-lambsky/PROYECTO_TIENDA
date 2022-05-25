from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
from sqlconnector import DAO

dao=DAO()
ventana=Tk()
ventana.title('La Tienda')
ventana.geometry("1330x600")
ventana.resizable (0,0)
ventana.rowconfigure(0,weight=1)
ventana.columnconfigure(0,weight=1)
icon=Image.open('IMAGES/LogoTienda.png')
icon=ImageTk.PhotoImage(icon)
ventana.iconphoto(True,icon)
user=StringVar()
password=StringVar()
level=StringVar()
options=["Escoja una Opcion","1","2","3",]
level.set(options[0])

#Creación frames
menuInicial = Frame(ventana)
menuRegistro = Frame(ventana)
menuTablaUsuarios = Frame(ventana)
menuLogin = Frame(ventana)
menuTablaProductos = Frame(ventana)
menuTablaClientes=Frame(ventana)
menuMenuTablas = Frame(ventana)

#Lista y Carga previa de los frames
frameList=[menuInicial,menuRegistro, menuTablaUsuarios, menuLogin, menuTablaProductos,menuTablaClientes, menuMenuTablas]
for frame in frameList:
    frame.grid(row=0,column=0,sticky="nsew")

#Funcion para dirigirse al frame segun el nombre
def framesManager(frameName):
    frameName.tkraise()

def cleanEntry(entry):
    entry.delete("0","end")

def cleanReturn(frameName,entry,entry2=None,entry3=None):
    cleanEntry(entry)
    if entry2!=None:
        cleanEntry(entry2)
    elif entry3!=None:
        cleanEntry(entry3)
    framesManager(frameName)

framesManager(menuInicial)

#imagenes
bgMenuInicial=Image.open('IMAGES/menuInicial.png')
resizedImg=bgMenuInicial.resize((1330,600))
bgMenuInicial=ImageTk.PhotoImage(resizedImg)

bgRegisterMenu=Image.open('IMAGES/REGISTRO.png')
resizedImg=bgRegisterMenu.resize((1330,600))
bgRegisterMenu=ImageTk.PhotoImage(resizedImg)

bgMenuTablaUsuarios=Image.open('IMAGES/tablaUsuarios.png')
resizedImg=bgMenuTablaUsuarios.resize((1330,600))
bgMenuTablaUsuarios=ImageTk.PhotoImage(resizedImg)

bgMenuLogin=Image.open('IMAGES/Login.png')
resizedImg=bgMenuLogin.resize((1330,600))
bgMenuLogin=ImageTk.PhotoImage(resizedImg)

bgMenuTablaProductos=Image.open('IMAGES/tablaProductos.png')
resizedImg=bgMenuTablaProductos.resize((1330,600))
bgMenuTablaProductos=ImageTk.PhotoImage(resizedImg)

bgMenuTablaClientes=Image.open('IMAGES/tablaProductos.png')
resizedImg=bgMenuTablaClientes.resize((1330,600))
bgMenuTablaClientes=ImageTk.PhotoImage(resizedImg)

bgMenuTablas=Image.open('IMAGES/menuTablas.png')
resizedImg=bgMenuTablas.resize((1330,600))
bgMenuTablas=ImageTk.PhotoImage(resizedImg)

#--------Creacion del fondo menu Inicial------
fondoMenuInicial=Label(menuInicial,image=bgMenuInicial).place(x=0,y=0,relheight=1,relwidth=1)

#Botones del menuInicial

btLogin = Button(menuInicial,text="INGRESAR",cursor="hand2",bg= "#57664E",width=22,height=2,relief="flat",fg="white",font=("Century Gothic",12),command=lambda:framesManager(menuLogin))
btLogin.place(x=280,y=305)
btRegister = Button(menuInicial,text="REGISTRARSE",cursor="hand2",bg= "#57664E",width=22,height=2,relief="flat",fg="white",font=("Century Gothic",12),command=lambda: framesManager(menuRegistro))
btRegister.place(x=880,y=305)

#-------------------MENU REGISTRO------------------------
def validateEntryUser(tex,new_text):
    if len(new_text) > 8:
        validation=False
    else:
        validation=True

    return validation

def validateEntryPassword(text,new_text):
    # Primero chequear que el contenido total no exceda los diez caracteres.
    if len(new_text) > 4:
        return False
    # Luego, si la validación anterior no falló, chequear que el texto solo
    # contenga números.
    return text.isdecimal()

def checkEmptyFieldsRegister(entry1,entry2,entry3):
    if len(entry1.get())==0:
        messagebox.showerror(title="Error!",message="El campo de usuario se encuentra vacio")
        return False
    elif len(entry2.get())==0:
        messagebox.showerror(title="Error!",message="El campo de contraseña se encuentra vacio")
        return False
    elif entry3.get()=="Escoja una Opcion":
        messagebox.showerror(title="Error!",message="El campo de nivel se encuentra vacio, escoja una opcion!")
        return False
    return True

def getNewUser():
    if checkEmptyFieldsRegister(entryUserName,entryPassword,level):
        usuario=(entryUserName.get(),int(entryPassword.get()),int(level.get()))
        dao.newUsuario(usuario)
        cleanEntry(entryUserName)
        cleanEntry(entryPassword)
        framesManager(menuInicial)

#-----Creacion del fondo de menuRegistro-----
fondoRegisterMenu=Label(menuRegistro,image=bgRegisterMenu).place(x=0,y=0,relheight=1,relwidth=1)

#Entry del menuRegistro
entryUserName=Entry(menuRegistro, textvariable=user, width=22, relief="flat", bg="#DBD0A1",fg="black",font=("Century Gothic",12))
entryUserName.config(validate='key',validatecommand=(ventana.register(validateEntryUser), "%S", "%P"))
entryUserName.place(x=460,y=255, height=30)

entryPassword=Entry(menuRegistro, textvariable=password, width=22, relief="flat", bg="#DBD0A1",fg="black",font=("Century Gothic",12),show="*")
entryPassword.config(validate='key',validatecommand=(ventana.register(validateEntryPassword), "%S", "%P"))
entryPassword.place(x=460,y=345, height=30)

#ComboBox del menuRegistro
levelBox = OptionMenu(menuRegistro,level,*options)
levelBox.place(x=420,y=400,width=500)

#Botones del menuRegistro
btNewUser = Button(menuRegistro,text="REGISTRAR",cursor="hand2",bg= "#57664E",width=15,height=1,relief="flat",fg="black",font=("Century Gothic",12),command=lambda:getNewUser())
btNewUser.place(x=485,y=465)
btReturn = Button(menuRegistro,text="REGRESAR",cursor="hand2",bg= "#57664E",width=15,height=1,relief="flat",fg="black",font=("Century Gothic",12),command=lambda: cleanReturn(menuInicial,entryPassword,entryUserName))
btReturn.place(x=700,y=465)

#-----------------------------------Menu Login------------------------------------------
#-------Creacion fondo de menuLogin-----
def checkEmptyFieldsLogin(entry1,entry2):
    if len(entry1.get())==0:
        messagebox.showerror(title="Error!",message="El campo de usuario se encuentra vacio")
        return False
    elif len(entry2.get())==0:
        messagebox.showerror(title="Error!",message="El campo de contraseña se encuentra vacio")
        return False
    return True

def login():
    if checkEmptyFieldsLogin(entryLoginUsuario,entryLoginPassword):
        if dao.login(entryLoginUsuario.get(),entryLoginPassword.get()):
            framesManager(menuMenuTablas)

fondoLogin =Label(menuLogin, image=bgMenuLogin).place(x=0,y=0,relheight=1,relwidth=1)

#Entry menuLogin
entryLoginUsuario=Entry(menuLogin,width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryLoginUsuario.config(validate='key',validatecommand=(ventana.register(validateEntryUser), "%S", "%P"))
entryLoginUsuario.place(x=460,y=280,height=30)

entryLoginPassword=Entry(menuLogin,width=22, relief="flat", bg="#DBD0A1",fg="black",font=("Century Gothic",12),show="*" )
entryLoginPassword.config(validate='key',validatecommand=(ventana.register(validateEntryPassword), "%S", "%P"))
entryLoginPassword.place(x=460,y=370,height=30)

#botones menuLogin

btLoginIngresar = Button(menuLogin, text= "INGRESAR",bg= "#57664E",width=15,height=1,relief="flat",fg="black",font=("Century Gothic",12),command=lambda:login())
btLoginIngresar.place(x=465,y=430)

btLoginRegresar = Button(menuLogin, text= "REGRESAR",bg= "#57664E",width=15,height=1,relief="flat",fg="black",font=("Century Gothic",12),command=lambda: cleanReturn(menuInicial,entryLoginPassword,entryLoginUsuario))
btLoginRegresar.place(x=700,y=430)
#menu Menu
fondoMenuMenu=Label(menuMenuTablas, image=bgMenuTablas).place(x=0,y=0,relheight=1,relwidth=1)

#botones menu menu

btMenuMenu=Button(menuMenuTablas, bg= "#57664E",width=12,height=1,relief="flat",fg="black",font=("Century Gothic",12),command=lambda:framesManager(menuTablaUsuarios))
btMenuMenu.place(x=465,y=430)

#-----------Creación tablas-------------
#Tabla usuarios
#----------fondo menu tabla usuarios------
fondoMenuTablaUsuarios=Label(menuTablaUsuarios, image=bgMenuTablaUsuarios).place(x=0,y=0,relheight=1,relwidth=1)

 
#entries menu tabla usuarios

entryMenuTablaUsuarios1=Entry(menuTablaUsuarios, width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryMenuTablaUsuarios1.place(x=360,y=170,height=30)

entryMenuTablaUsuarios2=Entry(menuTablaUsuarios, width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryMenuTablaUsuarios2.place(x=360,y=370,height=30)

entryMenuTablaUsuarios3=Entry(menuTablaUsuarios, width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryMenuTablaUsuarios3.place(x=360,y=570,height=30)

    #botones menu tabla usuarios
        #BOTON GUARDAR
btGuardarUsuario = Button(menuTablaUsuarios, text= "GUARDAR",bg= "#57664E",width=22,height=2,relief="flat",fg="white",font=("Century Gothic",12))
btGuardarUsuario.place(x=180,y=95)

        #BOTON ACTUALIZAR
btActualizarUsuario = Button(menuTablaUsuarios, text= "ACTUALIZAR",bg= "#57664E",width=22,height=2,relief="flat",fg="white",font=("Century Gothic",12))
btActualizarUsuario.place(x=180,y=205)

        #BOTON BORRAR
btBorrarUsuario = Button(menuTablaUsuarios, text= "BORRAR",bg= "#57664E",width=22,height=2,relief="flat",fg="white",font=("Century Gothic",12))
btBorrarUsuario.place(x=180,y=505)

        #CREACION TABLA
tablaUsuarios=ttk.Treeview(menuTablaUsuarios, columns=("col1", "col2"))


tablaUsuarios.column("#0",width=90, anchor=CENTER)
tablaUsuarios.column("col1",width=90, anchor=CENTER)
tablaUsuarios.column("col2",width=90, anchor=CENTER)

tablaUsuarios.heading("#0", text="NOMBRE", anchor=CENTER)
tablaUsuarios.heading("col1", text="CLAVE", anchor=CENTER)
tablaUsuarios.heading("col2", text="NIVEL", anchor=CENTER)

tablaUsuarios.place(x=810,y=150,width=520,height=280)

#prueba
tablaUsuarios.insert("",END, text="Nico", values=("","UNO"))


#-------------------------Tabla productos-------------------------------
#----------fondo menu tabla productos---------
fondoMenuTablaProductos=Label(menuTablaProductos, image=bgMenuTablaProductos).place(x=0,y=0,relheight=1,relwidth=1)

    #entries menu tabla productos

entryMenuTablaProductos1=Entry(menuTablaProductos, width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryMenuTablaProductos1.place(x=460,y=370,height=30)

entryMenuTablaProductos2=Entry(menuTablaProductos, width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryMenuTablaProductos2.place(x=460,y=470,height=30)

entryMenuTablaProductos3=Entry(menuTablaProductos, width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryMenuTablaProductos3.place(y=570,height=30)

    #botones menu tabla usuarios
        #BOTON GUARDAR
btGuardarProducto = Button(menuTablaProductos, text= "GUARDAR",bg= "#57664E",width=22,height=2,relief="flat",fg="white",font=("Century Gothic",12))
btGuardarProducto.place(x=180,y=95)

        #BOTON ACTUALIZAR
btActualizarProducto = Button(menuTablaProductos, text= "ACTUALIZAR",bg= "#57664E",width=22,height=2,relief="flat",fg="white",font=("Century Gothic",12))
btActualizarProducto.place(x=180,y=205)

        #BOTON BORRAR
btBorrarProducto = Button(menuTablaProductos, text= "BORRAR",bg= "#57664E",width=22,height=2,relief="flat",fg="white",font=("Century Gothic",12))
btBorrarProducto.place(x=180,y=505)

        #CREACION TABLA
tablaProducto=ttk.Treeview(menuTablaProductos, columns=("col1", "col2"))


tablaProducto.column("#0",width=90, anchor=CENTER)
tablaProducto.column("col1",width=90, anchor=CENTER)
tablaProducto.column("col2",width=90, anchor=CENTER)

tablaProducto.heading("#0", text="CÓDIGO PRODUCTO", anchor=CENTER)
tablaProducto.heading("col1", text="NOMBRE PRODUCTO", anchor=CENTER)
tablaProducto.heading("col2", text="PRECIO", anchor=CENTER)

tablaProducto.place(x=410,y=150,width=520,height=280)

#prueba
tablaProducto.insert("",END, text="PAPITAS", values=("","2.000"))

#-------------------------Tabla clientes-------------------------------
#----------fondo menu tabla clientes---------
fondoMenuTablaClientes=Label(menuTablaClientes, image=bgMenuTablaClientes).place(x=0,y=0,relheight=1,relwidth=1)

    #entries menu tabla productos

entryMenuTablaClientes1=Entry(menuTablaClientes, width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryMenuTablaClientes1.place(x=460,y=370,height=30)

entryMenuTablaClientes2=Entry(menuTablaClientes, width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryMenuTablaClientes2.place(x=460,y=470,height=30)

entryMenuTablaClientes3=Entry(menuTablaClientes, width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryMenuTablaClientes3.place(y=570,height=30)

    #botones menu tabla usuarios
        #BOTON GUARDAR
btGuardarCliente = Button(menuTablaClientes, text= "GUARDAR",bg= "#57664E",width=22,height=2,relief="flat",fg="white",font=("Century Gothic",12))
btGuardarCliente.place(x=180,y=95)

        #BOTON ACTUALIZAR
btActualizarClientes = Button(menuTablaClientes, text= "ACTUALIZAR",bg= "#57664E",width=22,height=2,relief="flat",fg="white",font=("Century Gothic",12))
btActualizarClientes.place(x=180,y=205)

        #BOTON BORRAR
btBorrarClientes = Button(menuTablaClientes, text= "BORRAR",bg= "#57664E",width=22,height=2,relief="flat",fg="white",font=("Century Gothic",12))
btBorrarClientes.place(x=180,y=505)

        #CREACION TABLA
tablaProducto=ttk.Treeview(menuTablaProductos, columns=("col1", "col2"))


tablaProducto.column("#0",width=90, anchor=CENTER)
tablaProducto.column("col1",width=90, anchor=CENTER)
tablaProducto.column("col2",width=90, anchor=CENTER)

tablaProducto.heading("#0", text="CÓDIGO PRODUCTO", anchor=CENTER)
tablaProducto.heading("col1", text="NOMBRE PRODUCTO", anchor=CENTER)
tablaProducto.heading("col2", text="PRECIO", anchor=CENTER)

tablaProducto.place(x=410,y=150,width=520,height=280)

#prueba
tablaProducto.insert("",END, text="PAPITAS", values=("","2.000"))
ventana.mainloop()
