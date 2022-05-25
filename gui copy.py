
from optparse import Option
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.font import Font
from conexion import DAO
from funciones import funciones
from tkinter import ttk


ventana=Tk()
ventana.title('Tienda')
ventana.geometry("1065x580")
ventana.resizable (0,0)
ventana.rowconfigure(0,weight=1)
ventana.columnconfigure(0,weight=1)

fuenteLetra= Font(
    family="Helvetica",
    size=20,
    weight="bold",
    slant="roman",
    underline=0,
    overstrike=0
)


dao= DAO() 
c= funciones()
id=-1
#Numero de paginas 

menuLogin= Frame(ventana)
menuRegistrar= Frame(ventana)
menuPrincipal= Frame(ventana)
menuUsuarios= Frame(ventana)
menuEliminarUsuario= Frame(ventana)
menuTablaProductos= Frame(ventana)
menuTablaClientes= Frame(ventana)
menuTablaVentas= Frame(ventana)
menuTablaProveedores = Frame (ventana)
menuTablaInventarios = Frame (ventana)

#Funcion for para cambiar de paginas 
framesList=[menuLogin, menuPrincipal,menuRegistrar, menuUsuarios,menuTablaProductos, menuTablaClientes,menuTablaVentas, menuTablaProveedores,menuTablaInventarios]
for frame in framesList:
    frame.grid(row=0,column=0,sticky="nsew")

def framesManager(frame_name):
        frame_name.tkraise()

framesManager(menuLogin)

#funciones get

def getNivelUsuario():
    global nivelUsuario
    nivelUsuario=clicked.get()
    return nivelUsuario


#funciones
def habilitarEntryU(estado):
    menuUsuarioEntryUsuarioTx.configure(state=estado)
    menuUsuarioEntryClaveTx.configure(state=estado)
    drop1.configure(state=estado)

def habilitarEntryC(estado):
    menuclientesTxCodigo.configure(state=estado)
    menuclientesTxNombre.configure(state=estado)
    menuclientesTxDireccion.configure(state=estado)
    menuclientesTxCiudad.configure(state=estado)
    menuclientesTxTelefono.configure(state=estado)


def habilitarEntryP(estado):
    menuproductosTxCodigo.configure(state=estado)
    menuproductosTxNombre.configure(state=estado)
    menuproductosTxCosto.configure(state=estado)
   

def limpiarTxU():
    menuUsuarioEntryUsuarioTx.delete(0,END)
    menuUsuarioEntryClaveTx.delete(0,END)

def limpiarTxC():
    menuclientesTxCodigo.delete(0,END)
    menuclientesTxNombre.delete(0,END)
    menuclientesTxDireccion.delete(0,END)
    menuclientesTxCiudad.delete(0,END)
    menuclientesTxTelefono.delete(0,END)
    
def limpiarTxP():
    menuproductosTxCodigo.delete(0,END)
    menuproductosTxNombre.delete(0,END)
    menuproductosTxCosto.delete(0,END)


def habilitarBtnOper(estado):
    menuUsuarioBtRegistrar.configure(state=estado)
    menuUsuarioBtEliminar.configure(state=estado)
    menuUsuarioBtActualizar.configure(state=estado)

def habilitarBtnOperCliente(estado):
    menuTablaClientesBtRegistrar.configure(state=estado)
    menuTablaClientesBtEliminar.configure(state=estado)
    menuTablaClientesBtActualizar.configure(state=estado)


def habilitarBtnOperProductos(estado):
    menuTablaProductosBtBtRegistrar.configure(state=estado)
    menuTablaProductosBtEliminar.configure(state=estado)
    menuTablaProductosBtActualizar.configure(state=estado)


def habilitarBtnGuardar(estado):
    menuUsuarioBtGuardar.configure(state=estado)
    menuUsuarioBtCancelar.configure(state=estado)

def habilitarBtnGuardarClientes(estado):
    menuTablaClientesBtGuardar.configure(state=estado)
    menuTablaClientesBtCancelar.configure(state=estado)

def habilitarBtnGuardarProductos(estado):
    menuTablaProductosBtGuardar.configure(state=estado)
    menuTablaProductosBtCancelar.configure(state=estado)

def limpiarTabla():
    for item in tablaUsuario.get_children():
        tablaUsuario.delete(item)

def limpiarTablaClientes():
    for item in tablaclientes.get_children():
        tablaclientes.delete(item)

def limpiarTablaProductos():
    for item in tablaproductos.get_children():
        tablaproductos.delete(item)

def cargarTabla():
    global a
    a=1
    datos=dao.consultarUsuarios()
    for row in datos:
            tablaUsuario.insert("",END,text=row[0], values=(row[1],row[2]))
    habilitarEntryU("disabled")
    habilitarBtnOper("normal")
    habilitarBtnGuardar("disabled")
    framesManager(menuUsuarios)

def cargarTablaClientes():
    global b
    b=1
    datos=dao.consultarClientes()
    for row in datos:
            tablaclientes.insert("",END,text=row[0], values=(row[1],row[3],row[4],row[2]))
    habilitarEntryC("disabled")
    habilitarBtnOperCliente("normal")
    habilitarBtnGuardarClientes("disabled")
    framesManager(menuTablaClientes)

def cargarTablaProductos():
    global c
    c=1
    datos=dao.consultarProductos()
    for row in datos:
            menuTablaProductos.insert("",END,text=row[0], values=(row[1],row[2]))
    habilitarEntryP("disabled")
    habilitarBtnOperProductos("normal")
    habilitarBtnGuardarProductos("disabled")
    framesManager(menuTablaProductos)

def usuarioNuevo():
    habilitarEntryU("normal")
    habilitarBtnOper("disabled")
    habilitarBtnGuardar("normal")
    limpiarTxU()
    menuUsuarioEntryUsuarioTx.focus()

def clienteNuevo():
    habilitarEntryC("normal")
    habilitarBtnOperCliente("disabled")
    habilitarBtnGuardarClientes("normal")
    limpiarTxC()
    menuclientesTxCodigo.focus()

def productoNuevo():
    habilitarEntryP("normal")
    habilitarBtnOperProductos("disabled")
    habilitarBtnGuardarProductos("normal")
    limpiarTxC()
    menuproductosTxCodigo.focus()

def fCancelar():
    limpiarTabla()
    limpiarTxU()
    framesManager(menuPrincipal)

def fCancelarCliente():
    limpiarTablaClientes()
    limpiarTxC()
    framesManager(menuPrincipal)

def fCancelarProducto():
    limpiarTablaProductos()
    limpiarTxC()
    framesManager(menuPrincipal)


def fGuardar():
    global a
    if a==1:
        dao.insertaUsuario(menuUsuarioEntryUsuarioTx.get(),menuUsuarioEntryClaveTx.get(),clicked1.get())
    else:
        dao.modificaUsuario(menuUsuarioEntryUsuarioTx.get(),menuUsuarioEntryClaveTx.get(),clicked1.get())
        a=1
    limpiarTabla()
    cargarTabla()
    limpiarTxU()
    habilitarBtnGuardar("disabled")
    habilitarBtnOper("normal")


def fGuardarCliente():
    global b
    if b==1:
        dao.insertaClientes(menuclientesTxCodigo.get(),menuclientesTxNombre.get(),menuclientesTxDireccion.get(),menuclientesTxTelefono.get(),menuclientesTxCiudad.get())
    else:
        dao.modificaClientes(menuclientesTxCodigo.get(),menuclientesTxNombre.get(),menuclientesTxDireccion.get(),menuclientesTxTelefono.get(),menuclientesTxCiudad.get())
        b=1
    limpiarTablaClientes()
    cargarTablaClientes()
    limpiarTxC()
    habilitarBtnGuardarClientes("disabled")
    habilitarBtnOperCliente("normal")



def fModificar():
    global a
    a=a+1
    selected = tablaUsuario.focus()
    clave = tablaUsuario.item(selected,'text')
    if clave == '':
        messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')
    else:
        habilitarEntryU("normal")
        nombre= tablaUsuario.item(selected,'text')
        valores = tablaUsuario.item(selected,'values')
        nivel= tablaUsuario.item(selected,'values')
        limpiarTxU()
        menuUsuarioEntryUsuarioTx.insert(0,nombre)
        menuUsuarioEntryClaveTx.insert(0,valores[0])
        clicked1.set(nivel[1])
        habilitarBtnOper("disabled")
        habilitarBtnGuardar("normal")
        menuUsuarioEntryUsuarioTx.focus()
    return True



def fModificarC():
    global b
    b=b+1
    selected = tablaclientes.focus()
    clave = tablaclientes.item(selected,'text')
    if clave == '':
        messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')
    else:
        habilitarEntryC("normal")
        codigo= tablaclientes.item(selected,'text')
        valores = tablaclientes.item(selected,'values')
        limpiarTxC()
        menuclientesTxCodigo.insert(0,codigo)
        menuclientesTxNombre.insert(0,valores[0])
        menuclientesTxTelefono.insert(0,valores[1])
        menuclientesTxCiudad.insert(0,valores[2])
        menuclientesTxDireccion.insert(0,valores[3])
        habilitarBtnOperCliente("disabled")
        habilitarBtnGuardarClientes("normal")
        menuclientesTxCodigo.focus()
    return True

def fEliminar():
    selected= tablaUsuario.focus()

    nombre= tablaUsuario.item(selected,'text')
    print(type(nombre))
    if nombre=="":
        messagebox.showinfo(title="Error", message="Seleccione un elemento")
    else:
        valores= tablaUsuario.item(selected,'values')
        data= str(nombre)+ "," + valores[0]+ ", " + valores[1]
        r=messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" +data)
        if r==messagebox.YES:
            n= dao.eliminaUsuario(nombre)
            if n ==1:
                messagebox.showinfo(title="Eliminado", message="Elemento eliminado correctamente")
                limpiarTabla()
                cargarTabla()
            else:
                messagebox.showinfo(title="Error", message="No fue posible eliminar el elemento seleccionado")

def fEliminarC():
    selected= tablaclientes.focus()

    codigo= tablaclientes.item(selected,'text')

    if codigo=="":
        messagebox.showinfo(title="Error", message="Seleccione un elemento")
    else:
        valores= tablaclientes.item(selected,'values')
        data= str(codigo)+ "," + valores[0]+ ", " + valores[1]+", " +valores[2]+", " +valores[3]
        r=messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" +data)
        if r==messagebox.YES:
            n= dao.eliminaClientes(codigo)
            if n ==1:
                messagebox.showinfo(title="Eliminado", message="Elemento eliminado correctamente")
                limpiarTablaClientes()
                cargarTablaClientes()
            else:
                messagebox.showinfo(title="Error", message="No fue posible eliminar el elemento seleccionado")


#Registo y login
def registrarU():
    usuario= c.pedirDatosRegistro(menuRegistrarEntryNombreTx.get(),menuRegistrarEntryContraseñaTx.get(),getNivelUsuario())
    try:
        dao.registrarUsuario(usuario)

    except Exception as e:
            print("Ocurrio un error.."+str(e))
    menuLoginEntryNombreTx.delete("0","end")
    menuLoginEntryContraseñaTx.delete("0","end")
    framesManager(menuPrincipal)

def loginU():
    try:
        if dao.login(menuLoginEntryNombreTx.get(),menuLoginEntryContraseñaTx.get())==True:
            framesManager(menuPrincipal)

    except Exception as e:
            print("Ocurrio un error.."+str(e))
    menuLoginEntryNombreTx.delete("0","end")
    menuLoginEntryContraseñaTx.delete("0","end")


#imagenes

bgMenuPrincipal= Image.open("Imagenes/fondoPrincipal.jpg")
resizeImagef=bgMenuPrincipal.resize((1065,580))
bgMenuPrincipal= ImageTk.PhotoImage(resizeImagef)

bgLogin= Image.open("Imagenes/login.png")
resizeImagef=bgLogin.resize((1065,580))
bgLogin= ImageTk.PhotoImage(resizeImagef)

bgRegistrar= Image.open("Imagenes/registrar.png")
resizeImagef=bgRegistrar.resize((1065,580))
bgRegistrar= ImageTk.PhotoImage(resizeImagef)

bgUsuarios= Image.open("Imagenes/tablaU.png")
resizeImagef=bgUsuarios.resize((1065,580))
bgUsuarios= ImageTk.PhotoImage(resizeImagef)

bgUsuariosEliminar= Image.open("Imagenes/fondoEliminarUsuario.png")
resizeImagef=bgUsuariosEliminar.resize((1065,580))
bgUsuariosEliminar= ImageTk.PhotoImage(resizeImagef)

bgmenuproductos = Image.open("Imagenes/menuproductos.png")
resizeImagef=bgmenuproductos.resize((1065,580))
bgmenuproductos= ImageTk.PhotoImage(resizeImagef)
 
bgmenuclientes = Image.open("Imagenes/menuClientes.png")
resizeImagef=bgmenuclientes.resize((1065,580))
bgmenuclientes= ImageTk.PhotoImage(resizeImagef)

bgmenuVentas = Image.open("Imagenes/manuVentas.png")
resizeImagef=bgmenuVentas.resize((1065,580))
bgmenuVentas= ImageTk.PhotoImage(resizeImagef)

bgmenuProveedores = Image.open("Imagenes/menuProveedores.png")
resizeImagef=bgmenuProveedores.resize((1065,580))
bgmenuProveedores= ImageTk.PhotoImage(resizeImagef)

bgmenuinventarios = Image.open("Imagenes/menuInventarios.png")
resizeImagef=bgmenuinventarios.resize((1065,580))
bgmenuinventarios= ImageTk.PhotoImage(resizeImagef)
#iconos 

bgIconoIngresar= Image.open("Imagenes/botonIngresar.png")
resizeImagef=bgIconoIngresar.resize((190,65))
bgIconoIngresar= ImageTk.PhotoImage(resizeImagef)

bgIconoRegistrarse= Image.open("Imagenes/iconoRegistrarse.png")
resizeImagef=bgIconoRegistrarse.resize((190,65))
bgIconoRegistrarse= ImageTk.PhotoImage(resizeImagef)

bgIconoUsuarios= Image.open("Imagenes/icono1.png")
resizeImagef=bgIconoUsuarios.resize((190,190))
bgIconoUsuarios= ImageTk.PhotoImage(resizeImagef)

bgIconoClientes= Image.open("Imagenes/iconoClientes.png")
resizeImagef=bgIconoClientes.resize((190,190))
bgIconoClientes= ImageTk.PhotoImage(resizeImagef)

bgIconoInventario= Image.open("Imagenes/iconoInventario.png")
resizeImagef=bgIconoInventario.resize((190,190))
bgIconoInventario= ImageTk.PhotoImage(resizeImagef)

bgIconoProductos= Image.open("Imagenes/iconoProductos.png")
resizeImagef=bgIconoProductos.resize((190,190))
bgIconoProductos= ImageTk.PhotoImage(resizeImagef)

bgIconoProveedores= Image.open("Imagenes/iconoProveedores.png")
resizeImagef=bgIconoProveedores.resize((190,190))
bgIconoProveedores= ImageTk.PhotoImage(resizeImagef)

bgIconoVentas= Image.open("Imagenes/iconoVentas.png")
resizeImagef=bgIconoVentas.resize((190,190))
bgIconoVentas= ImageTk.PhotoImage(resizeImagef)

bgIconoEliminar= Image.open("Imagenes/Eliminar.png")
resizeImagef=bgIconoEliminar.resize((190,190))
bgIconoEliminar= ImageTk.PhotoImage(resizeImagef)

bgIconoEliminarP= Image.open("Imagenes/Eliminar.png")
resizeImagef=bgIconoEliminarP.resize((60,60))
bgIconoEliminarP= ImageTk.PhotoImage(resizeImagef)


bgIconoActualizar= Image.open("Imagenes/Actualizar.png")
resizeImagef=bgIconoActualizar.resize((190,190))
bgIconoActualizar= ImageTk.PhotoImage(resizeImagef)

bgIconoActualizarP= Image.open("Imagenes/Actualizar.png")
resizeImagef=bgIconoActualizarP.resize((60,60))
bgIconoActualizarP= ImageTk.PhotoImage(resizeImagef)

bgIconoRegistrar= Image.open("Imagenes/botonRegistrar.png")
resizeImagef=bgIconoRegistrar.resize((190,190))
bgIconoRegistrar= ImageTk.PhotoImage(resizeImagef)

bgIconoRegistrarP= Image.open("Imagenes/botonRegistrar.png")
resizeImagef=bgIconoRegistrarP.resize((60,60))
bgIconoRegistrarP= ImageTk.PhotoImage(resizeImagef)

bgIconoMostrar= Image.open("Imagenes/mostrar.png")
resizeImagef=bgIconoMostrar.resize((190,190))
bgIconoMostrar= ImageTk.PhotoImage(resizeImagef)

bgIconoSalir= Image.open("Imagenes/Salir.png")
resizeImagef=bgIconoSalir.resize((90,60))
bgIconoSalir= ImageTk.PhotoImage(resizeImagef)

bgIconoCancelar= Image.open("Imagenes/botonCancelar.png")
resizeImagef=bgIconoCancelar.resize((100,40))
bgIconoCancelar= ImageTk.PhotoImage(resizeImagef)

bgIconoGuardar= Image.open("Imagenes/botonGuardar.png")
resizeImagef=bgIconoGuardar.resize((100,40))
bgIconoGuardar= ImageTk.PhotoImage(resizeImagef)



#menuLogin---------------------------------------------------------
#label


menuLoginFondo =Label(menuLogin,image=bgLogin)
menuLoginFondo.place(x=0,y=0)

#Entrys

menuLoginEntryNombreTx= Entry(menuLogin,width=29,font=fuenteLetra,border=0)
menuLoginEntryNombreTx.place(x=304,y=247)

menuLoginEntryContraseñaTx = Entry(menuLogin, show="*",width=29,font=fuenteLetra,border=0)
menuLoginEntryContraseñaTx.place(x=304,y=360)


#botones
menuLoginBtIngresar= Button(menuLogin,text="Ingresar",image=bgIconoIngresar,height=65,width=190, border=0, command= loginU)
menuLoginBtIngresar.place(x=290,y=440)

menuLoginBtRegistrar=Button(menuLogin,text="Registrarse",image=bgIconoRegistrarse,height=65,width=190, border=0, command= lambda: framesManager(menuRegistrar))
menuLoginBtRegistrar.place(x=550,y=440)


#menuRegistrar---------------------------------------------------------
#label

menuRegistrarFondo =Label(menuRegistrar,image=bgRegistrar)
menuRegistrarFondo.place(x=0,y=0)

options= ["1","2","3",]
clicked = StringVar()
clicked.set(options[0])
drop= OptionMenu(menuRegistrar, clicked, *options)
drop.place(x=630,y=450)
#Entrys

menuRegistrarEntryNombreTx= Entry(menuRegistrar,width=29,font=fuenteLetra,border=0)
menuRegistrarEntryNombreTx.place(x=304,y=247)

menuRegistrarEntryContraseñaTx = Entry(menuRegistrar, show="*",width=29,font=fuenteLetra,border=0)
menuRegistrarEntryContraseñaTx.place(x=304,y=360)


#botones/////////////////////////////////////////////////////////////////////

menuRegistrarBtRegistrar=Button(menuRegistrar,text="Registrarse",image=bgIconoRegistrarse,height=65,width=190, border=0, command= registrarU)
menuRegistrarBtRegistrar.place(x=290,y=440)


#menuPrincipal///////////////////////////////////////////////////////////////////////////////

menuPrincipalFondo =Label(menuPrincipal,image=bgMenuPrincipal)
menuPrincipalFondo.place(x=0,y=0)


menuLoginBtUsuarios= Button(menuPrincipal, height=190,width=190, image=bgIconoUsuarios, border=0,command= lambda: cargarTabla())
menuLoginBtUsuarios.place(x=150,y=90)

menuLoginBtProductos= Button(menuPrincipal, height=190,width=190, image=bgIconoProductos, border=0,command=lambda:cargarTablaProductos())
menuLoginBtProductos.place(x=400,y=90)

menuLoginBtClientes= Button(menuPrincipal, height=190,width=190, image=bgIconoClientes, border=0,command=lambda:cargarTablaClientes() )
menuLoginBtClientes.place(x=650,y=90)

menuLoginBtProveedores= Button(menuPrincipal, height=190,width=190, image=bgIconoProveedores, border=0)
menuLoginBtProveedores.place(x=150,y=340)

menuLoginBtInventarios= Button(menuPrincipal, height=190,width=190, image=bgIconoInventario, border=0)
menuLoginBtInventarios.place(x=400,y=340)

menuLoginBtVentas= Button(menuPrincipal, height=190,width=190, image=bgIconoVentas, border=0)
menuLoginBtVentas.place(x=650,y=340)



#menuUsuario Tabla///////////////////////////////////////////////////////////////////////////////////////7

menuUsuarioFondo =Label(menuUsuarios,image=bgUsuarios)
menuUsuarioFondo.place(x=0,y=0)


menuUsuarioEntryUsuarioTx= Entry(menuUsuarios,width=16,font=fuenteLetra,border=0)
menuUsuarioEntryUsuarioTx.place(x=150,y=247)

menuUsuarioEntryClaveTx = Entry(menuUsuarios, show="*",width=16,font=fuenteLetra,border=0)
menuUsuarioEntryClaveTx.place(x=150,y=360)


options1= ["1","2","3",]
clicked1 = StringVar()
clicked1.set(options1[0])
drop1= OptionMenu(menuUsuarios, clicked1, *options)
drop1.place(x=150,y=478,width=110)


menuUsuarioBtEliminar= Button(menuUsuarios, height=60,width=60, image=bgIconoEliminarP,command=fEliminar)
menuUsuarioBtEliminar.place(x=20,y=230)

menuUsuarioBtActualizar= Button(menuUsuarios, height=60,width=60, image=bgIconoActualizarP,command=fModificar)
menuUsuarioBtActualizar.place(x=20,y=330)

menuUsuarioBtRegistrar= Button(menuUsuarios, height=60,width=60, image=bgIconoRegistrarP,command=usuarioNuevo)
menuUsuarioBtRegistrar.place(x=20,y=430)

menuUsuarioBtCancelar= Button(menuUsuarios,width=100,height=40, border=0, image=bgIconoCancelar,command=fCancelar)
menuUsuarioBtCancelar.place(x=290,y=530)

menuUsuarioBtGuardar= Button(menuUsuarios,width=100,height=40, border=0, image=bgIconoGuardar,command=fGuardar)
menuUsuarioBtGuardar.place(x=150,y=530)


tablaUsuario=ttk.Treeview(menuUsuarios, columns=("col1","col2"))

tablaUsuario.column("#0",width=60, anchor=CENTER)
tablaUsuario.column("col1",width=90, anchor=CENTER)
tablaUsuario.column("col2",width=90, anchor=CENTER)

tablaUsuario.heading("#0", text="NOMBRE", anchor=CENTER)
tablaUsuario.heading("col1", text="CLAVE", anchor=CENTER)
tablaUsuario.heading("col2", text="NIVEL", anchor=CENTER)

tablaUsuario.place(x=410,y=150,width=620,height=400)

#menuproductos Tabla//////////////////////////////////////////////////////////////////////////////////////////////////////7

menuproductosFondo =Label(menuTablaProductos,image=bgmenuproductos)
menuproductosFondo.place(x=0,y=0)


menuproductosTxCodigo= Entry(menuTablaProductos,font=fuenteLetra,border=0)
menuproductosTxCodigo.place(x=150,y=161)

menuproductosTxNombre= Entry(menuTablaProductos,width=16,font=fuenteLetra,border=0)
menuproductosTxNombre.place(x=150,y=316)

menuproductosTxCosto= Entry(menuTablaProductos,width=16,font=fuenteLetra,border=0)
menuproductosTxCosto.place(x=150,y=516)


menuTablaProductosBtEliminar= Button(menuTablaProductos, height=60,width=60, image=bgIconoEliminarP)
menuTablaProductosBtEliminar.place(x=20,y=230)

menuTablaProductosBtActualizar= Button(menuTablaProductos, height=60,width=60, image=bgIconoActualizarP)
menuTablaProductosBtActualizar.place(x=20,y=330)

menuTablaProductosBtBtRegistrar= Button(menuTablaProductos, height=60,width=60, image=bgIconoRegistrarP)
menuTablaProductosBtBtRegistrar.place(x=20,y=430)

menuTablaProductosBtCancelar= Button(menuTablaProductos,width=100,height=40, border=0, image=bgIconoCancelar,command=lambda:framesManager(menuPrincipal))
menuTablaProductosBtCancelar.place(x=290,y=530)

menuTablaProductosBtGuardar= Button(menuTablaProductos,width=100,height=40, border=0, image=bgIconoGuardar,command=lambda:framesManager(menuPrincipal))
menuTablaProductosBtGuardar.place(x=150,y=530)


tablaproductos=ttk.Treeview(menuTablaProductos, columns=("col1","col2"))

tablaproductos.column("#0",width=60, anchor=CENTER)
tablaproductos.column("col1",width=90, anchor=CENTER)
tablaproductos.column("col2",width=90, anchor=CENTER)

tablaproductos.heading("#0", text="NOMBRE", anchor=CENTER)
tablaproductos.heading("col1", text="CLAVE", anchor=CENTER)
tablaproductos.heading("col2", text="NIVEL", anchor=CENTER)

tablaproductos.place(x=410,y=150,width=620,height=400)


#menuclientes Tabla////////////////////////////////////////////////////////////////////////7

menuclientesFondo =Label(menuTablaClientes,image=bgmenuclientes)
menuclientesFondo.place(x=0,y=0)


menuclientesTxCodigo= Entry(menuTablaClientes,width=13,font=fuenteLetra,border=0)
menuclientesTxCodigo.place(x=150,y=141)

menuclientesTxNombre= Entry(menuTablaClientes,width=17,font=fuenteLetra,border=0)
menuclientesTxNombre.place(x=150,y=220)

menuclientesTxTelefono= Entry(menuTablaClientes,width=17,font=fuenteLetra,border=0)
menuclientesTxTelefono.place(x=150,y=300)

menuclientesTxCiudad= Entry(menuTablaClientes,width=17,font=fuenteLetra,border=0)
menuclientesTxCiudad.place(x=150,y=380)

menuclientesTxDireccion= Entry(menuTablaClientes,width=17,font=fuenteLetra,border=0)
menuclientesTxDireccion.place(x=150,y=467)


menuTablaClientesBtEliminar= Button(menuTablaClientes, image=bgIconoEliminarP,command=fEliminarC)
menuTablaClientesBtEliminar.place(x=20,y=230)

menuTablaClientesBtActualizar= Button(menuTablaClientes, height=60,width=60, image=bgIconoActualizarP,command=fModificarC)
menuTablaClientesBtActualizar.place(x=20,y=330)

menuTablaClientesBtRegistrar= Button(menuTablaClientes, height=60,width=60, image=bgIconoRegistrarP,command=clienteNuevo)
menuTablaClientesBtRegistrar.place(x=20,y=430)

menuTablaClientesBtCancelar= Button(menuTablaClientes,width=100,height=40, border=0, image=bgIconoCancelar,command=fCancelarCliente)
menuTablaClientesBtCancelar.place(x=290,y=530)

menuTablaClientesBtGuardar= Button(menuTablaClientes,width=100,height=40, border=0, image=bgIconoGuardar,command=fGuardarCliente)
menuTablaClientesBtGuardar.place(x=150,y=530)


tablaclientes=ttk.Treeview(menuTablaClientes, columns=("col1","col2","col3","col4"))

tablaclientes.column("#0",width=60, anchor=CENTER)
tablaclientes.column("col1",width=90, anchor=CENTER)
tablaclientes.column("col2",width=90, anchor=CENTER)
tablaclientes.column("col3",width=90, anchor=CENTER)
tablaclientes.column("col4",width=90, anchor=CENTER)

tablaclientes.heading("#0", text="codclie", anchor=CENTER)
tablaclientes.heading("col1", text="nomclie", anchor=CENTER)
tablaclientes.heading("col2", text="telef", anchor=CENTER)
tablaclientes.heading("col3", text="ciudad", anchor=CENTER)
tablaclientes.heading("col4", text="direc", anchor=CENTER)

tablaclientes.place(x=410,y=150,width=620,height=400)

#menuventas Tabla////////////////////////////////////////////////////////////////////////////////////

menuVentasFondo =Label(menuTablaVentas,image=bgmenuproductos)
menuVentasFondo.place(x=0,y=0)

menuVentasTx= Entry(menuTablaVentas,font=fuenteLetra,border=0)
menuVentasTx.place(x=150,y=247)

menuVentasTx= Entry(menuTablaVentas,width=16,font=fuenteLetra,border=0)
menuVentasTx.place(x=150,y=360)
    
menuTablaVentasBtEliminar= Button(menuTablaVentas, image=bgIconoEliminarP)
menuTablaVentasBtEliminar.place(x=20,y=230)

menuTablaVentasBtActualizar= Button(menuTablaVentas, height=60,width=60, image=bgIconoActualizarP)
menuTablaVentasBtActualizar.place(x=20,y=330)

menuTablaVentasBtRegistrar= Button(menuTablaVentas, height=60,width=60, image=bgIconoRegistrarP)
menuTablaVentasBtRegistrar.place(x=20,y=430)

menuTablaVentasBtCancelar= Button(menuTablaVentas,width=100,height=40, border=0, image=bgIconoCancelar,command=lambda:framesManager(menuPrincipal))
menuTablaVentasBtCancelar.place(x=290,y=530)

menuTablaVentasBtGuardar= Button(menuTablaVentas,width=100,height=40, border=0, image=bgIconoGuardar,command=lambda:framesManager(menuPrincipal))
menuTablaVentasBtGuardar.place(x=150,y=530)


tablaVentas=ttk.Treeview(menuTablaVentas, columns=("col1","col2"))

tablaVentas.column("#0",width=60, anchor=CENTER)
tablaVentas.column("col1",width=90, anchor=CENTER)
tablaVentas.column("col2",width=90, anchor=CENTER)

tablaVentas.heading("#0", text="NOMBRE", anchor=CENTER)
tablaVentas.heading("col1", text="CLAVE", anchor=CENTER)
tablaVentas.heading("col2", text="NIVEL", anchor=CENTER)

tablaVentas.place(x=410,y=150,width=620,height=400)

#MENUPROVEEDORES Tabla////////////////////////////////////////////////////////////////////////////////////

menuProveedoresFondo =Label(menuTablaProveedores,image=bgmenuproductos)
menuProveedoresFondo.place(x=0,y=0)

menuProveedoresTxId= Entry(menuTablaProveedores,font=fuenteLetra,border=0)
menuProveedoresTxId.place(x=150,y=247)

menuProveedoresTxCodigo= Entry(menuTablaProveedores,width=16,font=fuenteLetra,border=0)
menuProveedoresTxCodigo.place(x=150,y=360)

menuProveedoresTxCosto= Entry(menuTablaProveedores,width=16,font=fuenteLetra,border=0)
menuProveedoresTxCosto.place(x=150,y=360)
    
menuTablaProveedoresBtEliminar= Button(menuTablaProveedores, image=bgIconoEliminarP)
menuTablaProveedoresBtEliminar.place(x=20,y=230)

menuTablaProveedoresBtActualizar= Button(menuTablaProveedores, height=60,width=60, image=bgIconoActualizarP)
menuTablaVentasBtActualizar.place(x=20,y=330)

menuTablaProveedoresBtRegistrar= Button(menuTablaProveedores, height=60,width=60, image=bgIconoRegistrarP)
menuTablaProveedoresBtRegistrar.place(x=20,y=430)

menuTablaProveedoresBtCancelar= Button(menuTablaProveedores,width=100,height=40, border=0, image=bgIconoCancelar,command=lambda:framesManager(menuPrincipal))
menuTablaProveedoresBtCancelar.place(x=290,y=530)

menuTablaProveedoresBtGuardar= Button(menuTablaProveedores,width=100,height=40, border=0, image=bgIconoGuardar,command=lambda:framesManager(menuPrincipal))
menuTablaProveedoresBtGuardar.place(x=150,y=530)


tablaProveedores=ttk.Treeview(menuTablaProveedores, columns=("col1","col2"))

tablaProveedores.column("#0",width=60, anchor=CENTER)
tablaProveedores.column("col1",width=90, anchor=CENTER)
tablaProveedores.column("col2",width=90, anchor=CENTER)

tablaProveedores.heading("#0", text="NOMBRE", anchor=CENTER)
tablaProveedores.heading("col1", text="CLAVE", anchor=CENTER)
tablaProveedores.heading("col2", text="NIVEL", anchor=CENTER)

tablaProveedores.place(x=410,y=150,width=620,height=400)

#MENUPROVEEDORES Tabla////////////////////////////////////////////////////////////////////////////////////

menuInventariosFondo =Label(menuTablaInventarios,image=bgmenuproductos)
menuInventariosFondo.place(x=0,y=0)

menuInventariosTx= Entry(menuTablaInventarios,font=fuenteLetra,border=0)
menuInventariosTx.place(x=150,y=247)

menuInventariosTx= Entry(menuTablaInventarios,width=16,font=fuenteLetra,border=0)
menuInventariosTx.place(x=150,y=360)
    
menuTablaInventariosBtEliminar= Button(menuTablaInventarios, image=bgIconoEliminarP)
menuTablaInventariosBtEliminar.place(x=20,y=230)

menuTablaInventariosBtActualizar= Button(menuTablaInventarios, height=60,width=60, image=bgIconoActualizarP)
menuTablaInventariosBtActualizar.place(x=20,y=330)

menuTablaInventariosBtRegistrar= Button(menuTablaInventarios, height=60,width=60, image=bgIconoRegistrarP)
menuTablaInventariosBtRegistrar.place(x=20,y=430)

menuTablaInventariosBtCancelar= Button(menuTablaInventarios,width=100,height=40, border=0, image=bgIconoCancelar,command=lambda:framesManager(menuPrincipal))
menuTablaInventariosBtCancelar.place(x=290,y=530)

menuTablaInventariosBtGuardar= Button(menuTablaInventarios,width=100,height=40, border=0, image=bgIconoGuardar,command=lambda:framesManager(menuPrincipal))
menuTablaInventariosBtGuardar.place(x=150,y=530)


tablaInventarios=ttk.Treeview(menuTablaInventarios, columns=("col1","col2"))

tablaInventarios.column("#0",width=60, anchor=CENTER)
tablaInventarios.column("col1",width=90, anchor=CENTER)
tablaInventarios.column("col2",width=90, anchor=CENTER)

tablaInventarios.heading("#0", text="NOMBRE", anchor=CENTER)
tablaInventarios.heading("col1", text="CLAVE", anchor=CENTER)
tablaInventarios.heading("col2", text="NIVEL", anchor=CENTER)

tablaInventarios.place(x=410,y=150,width=620,height=400)

ventana.mainloop()

