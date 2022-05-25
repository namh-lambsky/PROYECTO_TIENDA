from email import message
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='bmvhcreeqgnhyxzm530i-mysql.services.clever-cloud.com',
                port="3306",
                user="u0yq3gfszb886im2",
                password="Yho4kx1Frk5NGyNQyjWU",
                database="bmvhcreeqgnhyxzm530i"
            )
            print("Conexion exitosa")
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def __str__(self):
        datos=self.consultarUsuarios()
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux

    def __1str__(self):
        datos1=self.consultarClientes()
        aux=""
        for row in datos1:
            aux=aux + str(row) + "\n"
        return aux

    def __2str__(self):
        datos2=self.consultarProductos()
        aux=""
        for row in datos2:
            aux=aux + str(row) + "\n"
        return aux

    def consultarUsuarios(self):
        cur=self.conexion.cursor()
        cur.execute("SELECT * FROM usuarios")
        datos =cur.fetchall()
        cur.close()
        return datos

    def buscarUsuarios(self, nombre):
        cur = self.conexion.cursor()
        sql= "SELECT * FROM usuarios WHERE nomusu = {}".format(nombre)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos

    def insertaUsuario(self,nombre, clave, nivel):
        cur = self.conexion.cursor()
        sql='''INSERT INTO usuarios (nomusu, clave, nivel)
        VALUES('{}', '{}', '{}')'''.format(nombre, clave, nivel)
        cur.execute(sql)
        n=cur.rowcount
        self.conexion.commit()
        cur.close()
        return n

    def eliminaUsuario(self,nombre):
        cur = self.conexion.cursor()
        sql="DELETE FROM usuarios WHERE nomusu = '{}'".format(nombre)
        cur.execute(sql)
        n=cur.rowcount
        self.conexion.commit()
        cur.close()
        return n

    def modificaUsuario(self,nombre, clave, nivel):
        cur = self.conexion.cursor()
        sql="UPDATE usuarios SET clave='{1}', nivel='{2}' WHERE nomusu='{0}'".format(nombre, clave, nivel)
        cur.execute(sql)
        n=cur.rowcount
        self.conexion.commit()
        cur.close()
        return n





#Clientes/7////

    def consultarClientes(self):
        cur=self.conexion.cursor()
        cur.execute("SELECT * FROM clientes")
        datos1 =cur.fetchall()
        cur.close()
        return datos1

    def buscarClientes(self, codclie):
        cur = self.conexion.cursor()
        sql= "SELECT * FROM clientes WHERE codclie = {}".format(codclie)
        cur.execute(sql)
        datos1 = cur.fetchone()
        cur.close()
        return datos1

    def insertaClientes(self,codclie, nomclie, direc, telef, ciudad):
        cur = self.conexion.cursor()
        sql='''INSERT INTO clientes (codclie, nomclie, direc, telef, ciudad)
        VALUES('{0}', '{1}', '{2}','{3}','{4}')'''.format(codclie, nomclie, direc, telef, ciudad)
        cur.execute(sql)
        n=cur.rowcount
        self.conexion.commit()
        cur.close()
        return n

    def eliminaClientes(self,codclie):
        cur = self.conexion.cursor()
        sql="DELETE FROM clientes WHERE codclie = '{}'".format(codclie)
        cur.execute(sql)
        n=cur.rowcount
        self.conexion.commit()
        cur.close()
        return n

    def modificaClientes(self,codclie, nomclie, direc, telef, ciudad):
        cur = self.conexion.cursor()
        sql="UPDATE clientes SET nomclie='{1}', direc='{2}', telef='{3}', ciudad='{4}' WHERE codclie='{0}'".format(codclie, nomclie, direc, telef, ciudad)
        cur.execute(sql)
        n=cur.rowcount
        self.conexion.commit()
        cur.close()
        return n


#Productos
    def consultarProductos(self):
        cur=self.conexion.cursor()
        cur.execute("SELECT * FROM productos")
        datos2 =cur.fetchall()
        cur.close()
        return datos2

    def buscarProducto(self, codprod):
        cur = self.conexion.cursor()
        sql= "SELECT * FROM productos WHERE codprod = {}".format(codprod)
        cur.execute(sql)
        datos2 = cur.fetchone()
        cur.close()
        return datos2

    def insertarProducto(self,codprod, nomprod, costo):
        cur = self.conexion.cursor()
        sql='''INSERT INTO productos (codprod, nomprod, costo)
        VALUES('{0}', '{1}', '{2}')'''.format(codprod, nomprod, costo)
        cur.execute(sql)
        n=cur.rowcount
        self.conexion.commit()
        cur.close()
        return n

    def eliminarProducto(self,codprod):
        cur = self.conexion.cursor()
        sql="DELETE FROM productos WHERE codprod = '{}'".format(codprod)
        cur.execute(sql)
        n=cur.rowcount
        self.conexion.commit()
        cur.close()
        return n

    def modificarProducto(self,codprod, nomprod, costo):
        cur = self.conexion.cursor()
        sql="UPDATE productos SET nomprod='{1}', costo='{2}' WHERE codprod='{0}'".format(codprod, nomprod, costo)
        cur.execute(sql)
        n=cur.rowcount
        self.conexion.commit()
        cur.close()
        return n




    def registrarUsuario(self,usuario):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="INSERT INTO usuarios (nomusu, clave, nivel) VALUES ('{0}','{1}','{2}')"
                cursor.execute(sql.format(usuario[0], usuario[1], usuario[2]))
                self.conexion.commit()
                print("Curso registrado \n")

            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))


    def login(self,nombreUsuario,contraseña):
        cursor=self.conexion.cursor()
        cursor.execute("SELECT clave FROM usuarios WHERE nomusu='"+nombreUsuario+"'and clave='"+contraseña+"'")
        if cursor.fetchall():
            messagebox.showinfo(title="Inicio de sesion correcto", message="Usuario y contraseña correcta")
            return True
        else:
            messagebox.showinfo(title="Inicio de sesion incorrecto", message="Usuario y contraseña incorrecta")
            return False


