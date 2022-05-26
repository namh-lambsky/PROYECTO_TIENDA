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
levelU=StringVar()
options=["Escoja una Opcion","1","2","3",]
options1=["Escoja una Opcion","1","2","3",]
level.set(options[0])
levelU.set(options[0])

#Creación frames
menuInicial = Frame(ventana)
menuRegistro = Frame(ventana)
menuTablaUsuarios = Frame(ventana)
menuLogin = Frame(ventana)
menuTablaProductos = Frame(ventana)
menuTablaClientes=Frame(ventana)
menuMenuTablas = Frame(ventana)
menuTablaProveedores = Frame(ventana)

#Lista y Carga previa de los frames
frameList=[menuInicial,menuRegistro, menuTablaUsuarios, menuLogin, menuTablaProductos,menuTablaClientes, menuMenuTablas, menuTablaProveedores]
for frame in frameList:
    frame.grid(row=0,column=0,sticky="nsew")

#Funcion para dirigirse al frame segun el nombre
def framesManager(frameName):
    frameName.tkraise()

def cleanEntry(entry):
    entry.delete("0","end")

def cleanReturn(frameName,entry,entry2=None,entry3=None,entry4=None,entry5=None):
    cleanEntry(entry)
    if entry2!=None:
        cleanEntry(entry2)
    elif entry3!=None:
        cleanEntry(entry3)
    elif entry4!=None:
        cleanEntry(entry4)
    elif entry5!=None:
        cleanEntry(entry5)
    framesManager(frameName)

framesManager(menuInicial)

def limpiarTablas(tabla):
    if tabla == 1:
        for item in tablaUsuarios.get_children():
            tablaUsuarios.delete(item)
    elif tabla == 2:
        for item in tablaProducto.get_children():
            tablaProducto.delete(item)
    elif tabla ==3:
        for item in tablaClientes.get_children():
            tablaClientes.delete(item)
    elif tabla ==4:
        for item in tablaProveedores.get_children():
            tablaProveedores.delete(item)

def changeState(bt,state):
    if state==0:
        bt.configure(state="normal")
    if state==1:
        bt.configure(state="disabled")

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

bgMenuTablaClientes=Image.open('IMAGES/tablaCliente.png')
resizedImg=bgMenuTablaClientes.resize((1330,600))
bgMenuTablaClientes=ImageTk.PhotoImage(resizedImg)

bgMenuTablas=Image.open('IMAGES/menuTablas.png')
resizedImg=bgMenuTablas.resize((1330,600))
bgMenuTablas=ImageTk.PhotoImage(resizedImg)

bgMenuTablaProveedores=Image.open('IMAGES/proveedores.png')
resizedImg=bgMenuTablaProveedores.resize((1330,600))
bgMenuTablaProveedores=ImageTk.PhotoImage(resizedImg)


#--------Creacion del fondo menu Inicial------
fondoMenuInicial=Label(menuInicial,image=bgMenuInicial).place(x=0,y=0,relheight=1,relwidth=1)

#Botones del menuInicial

btLogin = Button(menuInicial,text="INGRESAR",cursor="hand2",bg= "#57664E",width=22,height=2,relief="flat",fg="white",font=("Century Gothic",12),command=lambda:framesManager(menuLogin))
btLogin.place(x=280,y=305)
btRegister = Button(menuInicial,text="REGISTRARSE",cursor="hand2",bg= "#57664E",width=22,height=2,relief="flat",fg="white",font=("Century Gothic",12),command=lambda: framesManager(menuRegistro))
btRegister.place(x=880,y=305)

#-------------------MENU REGISTRO------------------------
def validateEntryUser(text,new_text):
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

btLoginIngresar = Button(menuLogin, text= "INGRESAR",bg= "#DBD0A1",width=15,height=1,relief="flat",fg="black",font=("Century Gothic",12),command=lambda:login())
btLoginIngresar.place(x=465,y=430)

btLoginRegresar = Button(menuLogin, text= "REGRESAR",bg= "#DBD0A1",width=15,height=1,relief="flat",fg="black",font=("Century Gothic",12),command=lambda: cleanReturn(menuInicial,entryLoginPassword,entryLoginUsuario))
btLoginRegresar.place(x=700,y=430)
#menu Menu
fondoMenuMenu=Label(menuMenuTablas, image=bgMenuTablas).place(x=0,y=0,relheight=1,relwidth=1)

#botones menu menu

btMenuMenu1=Button(menuMenuTablas, bg= "#F2F4F3",width=5,height=1,relief="flat",fg="black",font=("Century Gothic",12),command=lambda:loadTablaUsuarios())
btMenuMenu1.place(x=755,y=30)

btMenuMenu2=Button(menuMenuTablas, bg= "#F2F4F3",width=5,height=1,relief="flat",fg="black",font=("Century Gothic",12),command=lambda:loadTablaProductos())
btMenuMenu2.place(x=755,y=140)

btMenuMenu3=Button(menuMenuTablas, bg= "#F2F4F3",width=5,height=1,relief="flat",fg="black",font=("Century Gothic",12),command=lambda:loadTablaClientes())
btMenuMenu3.place(x=755,y=240)

btMenuMenu4=Button(menuMenuTablas, bg= "#F2F4F3",width=5,height=1,relief="flat",fg="black",font=("Century Gothic",12),command=lambda:loadTablaProveedores())
btMenuMenu4.place(x=755,y=340)

#-----------Creación tablas-------------
#Tabla usuarios
#----------fondo menu tabla usuarios------
fondoMenuTablaUsuarios=Label(menuTablaUsuarios, image=bgMenuTablaUsuarios).place(x=0,y=0,relheight=1,relwidth=1)

def loadNewUsuario():
    changeState(entryMenuTablaUsuarios1,0)
    changeState(entryMenuTablaUsuarios2,0)
    changeState(levelBoxU,0)

def loadTablaUsuarios():
    global a
    a=1
    limpiarTablas(1)
    datos=dao.getTableInfo(1)
    for row in datos:
            tablaUsuarios.insert("",END,text=row[0], values=(row[1],row[2]))
    changeState(entryMenuTablaUsuarios1,1)
    changeState(entryMenuTablaUsuarios2,1)
    changeState(levelBoxU,1)
    changeState(btGuardarUsuario,0)
    changeState(btActualizarUsuario,0)
    changeState(btBorrarUsuario,0)
    framesManager(menuTablaUsuarios)

def guardarUsuario():
    global a
    usuario=(entryMenuTablaUsuarios1.get(),entryMenuTablaUsuarios2.get(),levelU.get())
    if a==1:
        dao.newUsuario(usuario)
    else:
        dao.updateUsuario(usuario)
        a=1
    cleanEntry(entryMenuTablaUsuarios1)
    cleanEntry(entryMenuTablaUsuarios2)
    changeState(entryMenuTablaUsuarios1,1)
    changeState(entryMenuTablaUsuarios2,1)
    changeState(levelBoxU,1)
    changeState(btGuardarUsuario,0)
    changeState(btActualizarUsuario,0)
    changeState(btBorrarUsuario,0)
    limpiarTablas(1)
    loadTablaUsuarios()

def modificarUsuario():
    global a
    a=a+1
    selected = tablaUsuarios.focus()
    clave = tablaUsuarios.item(selected,'text')
    if clave== '':
        messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')
    else:
        changeState(entryMenuTablaUsuarios1,0)
        changeState(entryMenuTablaUsuarios2,0)
        changeState(levelBoxU,0)
        valores = tablaUsuarios.item(selected,'values')
        nombre= tablaUsuarios.item(selected,'text')
        nivel= tablaUsuarios.item(selected,'values')
        cleanEntry(entryMenuTablaUsuarios1)
        cleanEntry(entryMenuTablaUsuarios2)
        entryMenuTablaUsuarios1.insert(0,nombre)
        entryMenuTablaUsuarios2.insert(0,valores[0])
        levelU.set(nivel[1])
        changeState(btGuardarUsuario,0)
        changeState(btActualizarUsuario,0)
        changeState(btBorrarUsuario,0)
        entryMenuTablaUsuarios1.focus()
    return True

def eliminarUsuario():
    selected= tablaUsuarios.focus()

    nombre= tablaUsuarios.item(selected,'text')
    if nombre=="":
        messagebox.showinfo(title="Error", message="Seleccione un elemento")
    else:
        valores= tablaUsuarios.item(selected,'values')
        data= str(nombre)+ ", " + valores[0]+ ", " + valores[1]
        r=messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" +data)
        if r==messagebox.YES:
            n = dao.deleteUsuario(nombre)
            if n == 1:
                messagebox.showinfo(title="Eliminado", message="Elemento eliminado correctamente")
                limpiarTablas(1)
            else:
                messagebox.showinfo(title="Error", message="No fue posible eliminar el elemento seleccionado")
    loadTablaUsuarios()

#entries menu tabla usuarios

entryMenuTablaUsuarios1=Entry(menuTablaUsuarios, width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryMenuTablaUsuarios1.place(x=160,y=230,height=30)

entryMenuTablaUsuarios2=Entry(menuTablaUsuarios, width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryMenuTablaUsuarios2.place(x=160,y=320,height=30)

levelBoxU = OptionMenu(menuTablaUsuarios,levelU,*options)
levelBoxU.place(x=160,y=400,width=200)

    #botones menu tabla usuarios
        #BOTON GUARDAR
btGuardarUsuario = Button(menuTablaUsuarios, text= "GUARDAR",bg= "#DBD0A1",width=12,height=1,relief="flat",fg="white",font=("Century Gothic",12),command=loadNewUsuario)
btGuardarUsuario.place(x=300,y=520)

        #BOTON ACTUALIZAR
btActualizarUsuario = Button(menuTablaUsuarios, text= "ACTUALIZAR",bg= "#DBD0A1",width=12,height=1,relief="flat",fg="white",font=("Century Gothic",12),command=modificarUsuario)
btActualizarUsuario.place(x=650,y=519)

        #BOTON BORRAR
btBorrarUsuario = Button(menuTablaUsuarios, text= "BORRAR",bg= "#DBD0A1",width=12,height=1,relief="flat",fg="white",font=("Century Gothic",12),command=eliminarUsuario)
btBorrarUsuario.place(x=1000,y=520)

#Boton regresar
btRegresarMenuUsuario = Button(menuTablaUsuarios, text= "REGRESAR",bg= "#DBD0A1",width=12,height=1,relief="flat",fg="white",font=("Century Gothic",12),command=lambda: cleanReturn(menuMenuTablas, entryMenuTablaUsuarios1, entryMenuTablaUsuarios2))
btRegresarMenuUsuario.place(x=140,y=450)

#Boton guardar registro
btGuardarMenuUsuario = Button(menuTablaUsuarios, text= "GUARDAR",bg= "#DBD0A1",width=12,height=1,relief="flat",fg="white",font=("Century Gothic",12),command=guardarUsuario)
btGuardarMenuUsuario.place(x=290,y=450)

        #CREACION TABLA
tablaUsuarios=ttk.Treeview(menuTablaUsuarios, columns=("col1", "col2"))


tablaUsuarios.column("#0",width=90, anchor=CENTER)
tablaUsuarios.column("col1",width=90, anchor=CENTER)
tablaUsuarios.column("col2",width=90, anchor=CENTER)

tablaUsuarios.heading("#0", text="NOMBRE", anchor=CENTER)
tablaUsuarios.heading("col1", text="CLAVE", anchor=CENTER)
tablaUsuarios.heading("col2", text="NIVEL", anchor=CENTER)

tablaUsuarios.place(x=510,y=195,width=520,height=280)

#-------------------------Tabla productos-------------------------------
def loadNewProducto():
    changeState(entryMenuTablaProductos1,0)
    changeState(entryMenuTablaProductos2,0)
    changeState(entryMenuTablaProductos3,0)

def loadTablaProductos():
    global b
    b=1
    limpiarTablas(2)
    datos=dao.getTableInfo(2)
    for row in datos:
            tablaProducto.insert("",END,text=row[0], values=(row[1],row[2]))
    changeState(entryMenuTablaProductos1,1)
    changeState(entryMenuTablaProductos2,1)
    changeState(entryMenuTablaProductos3,1)
    changeState(btGuardarProducto,0)
    changeState(btActualizarProducto,0)
    changeState(btBorrarProducto,0)
    framesManager(menuTablaProductos)

def guardarProducto():
    global b
    producto=(entryMenuTablaProductos1.get(),entryMenuTablaProductos2.get(),entryMenuTablaProductos3.get())
    if b==1:
        dao.newProducto(producto)
    else:
        dao.updateProducto(producto)
        b=1
    cleanEntry(entryMenuTablaProductos1)
    cleanEntry(entryMenuTablaProductos2)
    cleanEntry(entryMenuTablaProductos3)
    changeState(entryMenuTablaProductos1,1)
    changeState(entryMenuTablaProductos2,1)
    changeState(entryMenuTablaProductos3,1)
    changeState(btGuardarProducto,0)
    changeState(btActualizarProducto,0)
    changeState(btBorrarProducto,0)
    limpiarTablas(2)
    loadTablaProductos()

def modificarProducto():
    global b
    b=b+1
    selected = tablaProducto.focus()
    codprod = tablaProducto.item(selected,'text')
    if codprod== '':
        messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')
    else:
        changeState(entryMenuTablaProductos1,0)
        changeState(entryMenuTablaProductos2,0)
        changeState(entryMenuTablaProductos3,0)
        valores = tablaProducto.item(selected,'values')
        nombre= tablaProducto.item(selected,'text')
        cleanEntry(entryMenuTablaProductos1)
        cleanEntry(entryMenuTablaProductos2)
        cleanEntry(entryMenuTablaProductos3)
        entryMenuTablaProductos1.insert(0,nombre)
        entryMenuTablaProductos2.insert(0,valores[0])
        entryMenuTablaProductos3.insert(0,valores[1])
        changeState(btGuardarProducto,0)
        changeState(btActualizarProducto,0)
        changeState(btBorrarProducto,0)
        entryMenuTablaProveedores1.focus()
    return True

def eliminarProducto():
    selected= tablaProducto.focus()

    nombre= tablaProducto.item(selected,'text')
    if nombre=="":
        messagebox.showinfo(title="Error", message="Seleccione un elemento")
    else:
        valores= tablaProducto.item(selected,'values')
        data= str(nombre)+ ", " + valores[0]+ ", " + valores[1]
        r=messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" +data)
        if r==messagebox.YES:
            n = dao.deleteProducto(nombre)
            if n == 1:
                messagebox.showinfo(title="Eliminado", message="Elemento eliminado correctamente")
                limpiarTablas(1)
            else:
                messagebox.showinfo(title="Error", message="No fue posible eliminar el elemento seleccionado")
    loadTablaProductos()

#----------fondo menu tabla productos---------
fondoMenuTablaProductos=Label(menuTablaProductos, image=bgMenuTablaProductos).place(x=0,y=0,relheight=1,relwidth=1)

    #entries menu tabla productos

entryMenuTablaProductos1=Entry(menuTablaProductos, width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryMenuTablaProductos1.place(x=160,y=200,height=30)

entryMenuTablaProductos2=Entry(menuTablaProductos, width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryMenuTablaProductos2.place(x=160,y=300,height=30)

entryMenuTablaProductos3=Entry(menuTablaProductos, width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryMenuTablaProductos3.place(x=160,y=400,height=30)

    #botones menu tabla usuarios
        #BOTON GUARDAR
btGuardarProducto = Button(menuTablaProductos, text= "GUARDAR",bg= "#DBD0A1",width=12,height=1,relief="flat",fg="white",font=("Century Gothic",12),command=loadNewProducto)
btGuardarProducto.place(x=300,y=520)

        #BOTON ACTUALIZAR
btActualizarProducto = Button(menuTablaProductos, text= "ACTUALIZAR",bg= "#DBD0A1",width=12,height=1,relief="flat",fg="white",font=("Century Gothic",12),command=modificarProducto)
btActualizarProducto.place(x=650,y=519)

        #BOTON BORRAR
btBorrarProducto = Button(menuTablaProductos, text= "BORRAR",bg= "#DBD0A1",width=12,height=1,relief="flat",fg="white",font=("Century Gothic",12), command=eliminarProducto)
btBorrarProducto.place(x=1000,y=520)

btRegresarMenuProducto = Button(menuTablaProductos, text= "REGRESAR",bg= "#DBD0A1",width=12,height=1,relief="flat",fg="white",font=("Century Gothic",12),command=lambda: cleanReturn(menuMenuTablas, entryMenuTablaProductos1, entryMenuTablaProductos2,entryMenuTablaProductos3))
btRegresarMenuProducto.place(x=140,y=450)

#Boton guardar registro
btGuardarMenuProducto = Button(menuTablaProductos, text= "GUARDAR",bg= "#DBD0A1",width=12,height=1,relief="flat",fg="white",font=("Century Gothic",12),command=guardarProducto)
btGuardarMenuProducto.place(x=290,y=450)

        #CREACION TABLA
tablaProducto=ttk.Treeview(menuTablaProductos, columns=("col1", "col2"))


tablaProducto.column("#0",width=90, anchor=CENTER)
tablaProducto.column("col1",width=90, anchor=CENTER)
tablaProducto.column("col2",width=90, anchor=CENTER)

tablaProducto.heading("#0", text="CÓDIGO PRODUCTO", anchor=CENTER)
tablaProducto.heading("col1", text="NOMBRE PRODUCTO", anchor=CENTER)
tablaProducto.heading("col2", text="PRECIO", anchor=CENTER)

tablaProducto.place(x=510,y=195,width=520,height=280)

#-------------------------Tabla clientes-------------------------------

def loadNewCliente():
    changeState(entryMenuTablaClientes1,0)
    changeState(entryMenuTablaClientes2,0)
    changeState(entryMenuTablaClientes3,0)
    changeState(entryMenuTablaClientes4,0)
    changeState(entryMenuTablaClientes5,0)

def loadTablaClientes():
    global t
    t=1
    limpiarTablas(3)
    datos=dao.getTableInfo(3)
    for row in datos:
        tablaProducto.insert("",END,text=row[0], values=(row[1],row[2],row[3],row[4]))
    changeState(entryMenuTablaClientes1,1)
    changeState(entryMenuTablaClientes2,1)
    changeState(entryMenuTablaClientes3,1)
    changeState(entryMenuTablaClientes4,1)
    changeState(entryMenuTablaClientes5,1)
    changeState(btGuardarCliente,0)
    changeState(btActualizarClientes,0)
    changeState(btBorrarClientes,0)
    framesManager(menuTablaClientes)

def guardarCliente():
    global t
    cliente=(entryMenuTablaClientes1.get(),entryMenuTablaClientes2.get(),entryMenuTablaClientes3.get(),entryMenuTablaClientes4.get(),entryMenuTablaClientes5.get())
    if t==1:
        dao.newCliente(cliente)
    else:
        dao.updateCliente(cliente)
        t=1
    cleanEntry(entryMenuTablaClientes1)
    cleanEntry(entryMenuTablaClientes2)
    cleanEntry(entryMenuTablaClientes3)
    cleanEntry(entryMenuTablaClientes4)
    cleanEntry(entryMenuTablaClientes5)
    changeState(entryMenuTablaClientes1,1)
    changeState(entryMenuTablaClientes2,1)
    changeState(entryMenuTablaClientes3,1)
    changeState(entryMenuTablaClientes4,1)
    changeState(entryMenuTablaClientes5,1)
    changeState(btGuardarCliente,0)
    changeState(btActualizarClientes,0)
    changeState(btBorrarClientes,0)
    limpiarTablas(3)
    loadTablaClientes()

def modificarCliente():
    global t
    t=t+1
    selected = tablaClientes.focus()
    codclie = tablaClientes.item(selected,'text')
    if codclie== '':
        messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')
    else:
        changeState(entryMenuTablaClientes1,0)
        changeState(entryMenuTablaClientes2,0)
        changeState(entryMenuTablaClientes3,0)
        changeState(entryMenuTablaClientes4,0)
        changeState(entryMenuTablaClientes5,0)
        valores = tablaClientes.item(selected,'values')
        nombre= tablaClientes.item(selected,'text')
        cleanEntry(entryMenuTablaClientes1)
        cleanEntry(entryMenuTablaClientes2)
        cleanEntry(entryMenuTablaClientes3)
        cleanEntry(entryMenuTablaClientes4)
        cleanEntry(entryMenuTablaClientes5)
        entryMenuTablaClientes1.insert(0,nombre)
        entryMenuTablaClientes2.insert(0,valores[0])
        entryMenuTablaClientes3.insert(0,valores[1])
        entryMenuTablaClientes4.insert(0,valores[2])
        entryMenuTablaClientes5.insert(0,valores[3])
        changeState(btGuardarUsuario,0)
        changeState(btActualizarUsuario,0)
        changeState(btBorrarUsuario,0)
        entryMenuTablaUsuarios1.focus()
    return True

def eliminarCliente():
    selected= tablaClientes.focus()
    nombre= tablaClientes.item(selected,'text')
    if nombre=="":
        messagebox.showinfo(title="Error", message="Seleccione un elemento")
    else:
        valores= tablaClientes.item(selected,'values')
        data= str(nombre)+ ", " + valores[0]+ ", " + valores[1]
        r=messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" +data)
        if r==messagebox.YES:
            n = dao.deleteClientes(nombre)
            if n == 1:
                messagebox.showinfo(title="Eliminado", message="Elemento eliminado correctamente")
                limpiarTablas(1)
            else:
                messagebox.showinfo(title="Error", message="No fue posible eliminar el elemento seleccionado")
    loadTablaClientes()

#----------fondo menu tabla clientes---------
fondoMenuTablaClientes=Label(menuTablaClientes, image=bgMenuTablaClientes).place(x=0,y=0,relheight=1,relwidth=1)

    #entries menu tabla productos

entryMenuTablaClientes1=Entry(menuTablaClientes, width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryMenuTablaClientes1.place(x=160,y=200,height=30)

entryMenuTablaClientes2=Entry(menuTablaClientes, width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryMenuTablaClientes2.place(x=160,y=270,height=30)

entryMenuTablaClientes3=Entry(menuTablaClientes, width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryMenuTablaClientes3.place(x=160,y=340,height=30)

entryMenuTablaClientes4=Entry(menuTablaClientes, width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryMenuTablaClientes4.place(x=160,y=410,height=30)

entryMenuTablaClientes5=Entry(menuTablaClientes, width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryMenuTablaClientes5.place(x=160,y=470,height=30)

    #botones menu tabla clientes
        #BOTON GUARDAR
btGuardarCliente = Button(menuTablaClientes, text= "GUARDAR",bg= "#DBD0A1",width=12,height=1,relief="flat",fg="white",font=("Century Gothic",12),command=loadNewCliente)
btGuardarCliente.place(x=340,y=520)

        #BOTON ACTUALIZAR
btActualizarClientes = Button(menuTablaClientes, text= "ACTUALIZAR",bg= "#DBD0A1",width=12,height=1,relief="flat",fg="white",font=("Century Gothic",12),command=modificarCliente)
btActualizarClientes.place(x=660,y=519)

        #BOTON BORRAR
btBorrarClientes = Button(menuTablaClientes, text= "BORRAR",bg= "#DBD0A1",width=12,height=1,relief="flat",fg="white",font=("Century Gothic",12),command= eliminarCliente)
btBorrarClientes.place(x=1000,y=520)

btRegresarMenuClientes = Button(menuTablaClientes, text= "REGRESAR",bg= "#DBD0A1",width=12,height=1,relief="flat",fg="white",font=("Century Gothic",12),command=lambda: cleanReturn(menuMenuTablas, entryMenuTablaClientes1, entryMenuTablaClientes2,entryMenuTablaClientes3,entryMenuTablaClientes4,entryMenuTablaClientes5))
btRegresarMenuClientes.place(x=1080,y=450)

#Boton guardar registro
btGuardarMenuClientes = Button(menuTablaClientes, text= "GUARDAR",bg= "#DBD0A1",width=12,height=1,relief="flat",fg="white",font=("Century Gothic",12),command=guardarCliente)
btGuardarMenuClientes.place(x=1080,y=350)

        #CREACION TABLA
tablaClientes=ttk.Treeview(menuTablaClientes, columns=("col1", "col2", "col3", "col4"))


tablaClientes.column("#0",width=90, anchor=CENTER)
tablaClientes.column("col1",width=90, anchor=CENTER)
tablaClientes.column("col2",width=90, anchor=CENTER)
tablaClientes.column("col3",width=90, anchor=CENTER)
tablaClientes.column("col4",width=90, anchor=CENTER)

tablaClientes.heading("#0", text="CÓDIGO CLIENTE", anchor=CENTER)
tablaClientes.heading("col1", text="NOMBRE CLIENTE", anchor=CENTER)
tablaClientes.heading("col2", text="DIRECCION", anchor=CENTER)
tablaClientes.heading("col3", text="TELÉFONO", anchor=CENTER)
tablaClientes.heading("col4", text="CIUDAD", anchor=CENTER)

tablaClientes.place(x=510,y=195,width=520,height=280)

#-------------------------Tabla provedores-------------------------------
#----------fondo menu tabla provedores---------

def loadNewProveedores():
    changeState(entryMenuTablaProveedores1,0)
    changeState(entryMenuTablaProveedores2,0)
    changeState(entryMenuTablaProveedores3,0)

def loadTablaProveedores():
    global d
    d=1
    limpiarTablas(4)
    datos=dao.getTableInfo(4)
    for row in datos:
            tablaProveedores.insert("",END,text=row[0], values=(row[1],row[2]))
    changeState(entryMenuTablaProveedores1,1)
    changeState(entryMenuTablaProveedores2,1)
    changeState(entryMenuTablaProveedores3,1)
    changeState(btGuardarProveedores,0)
    changeState(btActualizarProveedores,0)
    changeState(btBorrarProveedores,0)
    framesManager(menuTablaProveedores)

def guardarProveedores():
    global d
    proveedor=(entryMenuTablaProveedores1.get(),entryMenuTablaProveedores2.get(),entryMenuTablaProveedores3.get())
    if d==1:
        dao.newProveedor(proveedor)
    else:
        dao.updateProvedor(proveedor)
        d=1
    cleanEntry(entryMenuTablaProveedores1)
    cleanEntry(entryMenuTablaProveedores2)
    cleanEntry(entryMenuTablaProveedores3)
    changeState(entryMenuTablaProveedores1,1)
    changeState(entryMenuTablaProveedores2,1)
    changeState(entryMenuTablaProveedores3,1)
    changeState(btGuardarProveedores,0)
    changeState(btActualizarProveedores,0)
    changeState(btBorrarProveedores,0)
    limpiarTablas(4)
    loadTablaProveedores()

def modificarProveedores():
    global d
    d=d+1
    selected = tablaProveedores.focus()
    codprod = tablaProveedores.item(selected,'text')
    if codprod== '':
        messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')
    else:
        changeState(entryMenuTablaProveedores1,0)
        changeState(entryMenuTablaProveedores2,0)
        changeState(entryMenuTablaProveedores3,0)
        valores = tablaProveedores.item(selected,'values')
        nombre= tablaProveedores.item(selected,'text')
        cleanEntry(entryMenuTablaProveedores1)
        cleanEntry(entryMenuTablaProductos2)
        cleanEntry(entryMenuTablaProductos3)
        entryMenuTablaProveedores1.insert(0,nombre)
        entryMenuTablaProveedores2.insert(0,valores[0])
        entryMenuTablaProveedores3.insert(0,valores[1])
        changeState(btGuardarProveedores,0)
        changeState(btActualizarProveedores,0)
        changeState(btBorrarProveedores,0)
        entryMenuTablaProveedores1.focus()
    return True

def eliminarProveedore():
    selected= tablaProveedores.focus()

    nombre= tablaProveedores.item(selected,'text')
    if nombre=="":
        messagebox.showinfo(title="Error", message="Seleccione un elemento")
    else:
        valores= tablaProveedores.item(selected,'values')
        data= str(nombre)+ ", " + valores[0]+ ", " + valores[1]
        r=messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" +data)
        if r==messagebox.YES:
            n = dao.deleteProveedor(nombre)
            if n == 1:
                messagebox.showinfo(title="Eliminado", message="Elemento eliminado correctamente")
                limpiarTablas(1)
            else:
                messagebox.showinfo(title="Error", message="No fue posible eliminar el elemento seleccionado")
    loadTablaProveedores()

fondoMenuTablaProveedores=Label(menuTablaProveedores, image=bgMenuTablaProveedores).place(x=0,y=0,relheight=1,relwidth=1)

    #entries menu tabla productos

entryMenuTablaProveedores1=Entry(menuTablaProveedores, width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryMenuTablaProveedores1.place(x=160,y=235,height=30)

entryMenuTablaProveedores2=Entry(menuTablaProveedores, width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryMenuTablaProveedores2.place(x=160,y=315,height=30)

entryMenuTablaProveedores3=Entry(menuTablaProveedores, width=22, relief="flat", bg="#DBD0A1" ,fg="black",font=("Century Gothic",12))
entryMenuTablaProveedores3.place(x=160,y=410,height=30)

    #botones menu tabla usuarios
        #BOTON GUARDAR
btGuardarProveedores= Button(menuTablaProveedores, text= "GUARDAR",bg= "#DBD0A1",width=12,height=1,relief="flat",fg="white",font=("Century Gothic",12))
btGuardarProveedores.place(x=300,y=520)

        #BOTON ACTUALIZAR
btActualizarProveedores = Button(menuTablaProveedores, text= "ACTUALIZAR",bg= "#DBD0A1",width=12,height=1,relief="flat",fg="white",font=("Century Gothic",12))
btActualizarProveedores.place(x=650,y=519)

        #BOTON BORRAR
btBorrarProveedores = Button(menuTablaProveedores, text= "BORRAR",bg= "#DBD0A1",width=12,height=1,relief="flat",fg="white",font=("Century Gothic",12))
btBorrarProveedores.place(x=1000,y=520)

        #CREACION TABLA
tablaProveedores=ttk.Treeview(menuTablaProveedores, columns=("col1", "col2"))


tablaProveedores.column("#0",width=90, anchor=CENTER)
tablaProveedores.column("col1",width=90, anchor=CENTER)
tablaProveedores.column("col2",width=90, anchor=CENTER)

tablaProveedores.heading("#0", text="CÓDIGO PROVEEDOR", anchor=CENTER)
tablaProveedores.heading("col1", text="CÓDIGO PRODUCTO", anchor=CENTER)
tablaProveedores.heading("col2", text="PRECIO", anchor=CENTER)

tablaProveedores.place(x=510,y=195,width=520,height=280)

#prueba
tablaProveedores.insert("",END, text="UNO", values=("UNO","1.000"))
ventana.mainloop()
