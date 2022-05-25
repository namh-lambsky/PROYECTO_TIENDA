import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

class DAO():
    def __init__(self):
        try:
            self.shopDB= mysql.connector.connect(
                host="bmjk6s1gngsf3waijgnl-mysql.services.clever-cloud.com",
                port="3306",
                user="ujaa9ecs1bdftwgs",
                password="HJ4IJhueoofnVC5pWD4J",
                database="beeinbbkp6stwtb9ybrl"
            )
            self.cursor=self.shopDB.cursor()
        except Exception as ex:
            print(ex)

#funcion encargada de retornar la informacion de la DB segun la tabla requerida
    def getTableInfo(self,table):
        if table==1:
            try:
                self.cursor.execute("SELECT * FROM Usuarios")
                result=self.cursor.fetchall()
                return result
            except Exception as ex:
                print("Error al intentar la conexión: {0}".format(ex))
        elif table==2:
            pass
#--------------------------------------Funciones Cliente----------------------------------------------
#Crea un usuario apartir de un objeto llamado usuario
    def newUsuario(self,usuario):
        try:
            sqlInstruction="INSERT INTO Usuarios(nomusu,clave,nivel) VALUES('{0}', '{1}', '{2}')"
            self.cursor.execute(sqlInstruction.format(usuario[0],usuario[1],usuario[2]))
            self.shopDB.commit()
        except Exception as ex:
            print("Error al intentar la conexión: {0}".format(ex))
#Actualiza un usuario ya existente apartir de un objeto llamado usuario
    def updateUsuario(self,usuario):
        try:
            sqlInstruction="UPDATE Usuarios SET clave='{1}', nivel='{2}' WHERE nomusu='{0}'"
            self.cursor.execute(sqlInstruction.format(usuario[0],usuario[1],usuario[2]))
            self.shopDB.commit()
        except Exception as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def deleteUsuario(self,nomusu):
        try:
            sqlinstrution="DELETE FROM Usuarios WHERE nomusu='{0}'"
            self.cursor.execute(sqlinstrution.format(nomusu))
            self.shopDB.commit()
            n=self.cursor.rowcount
            return n
        except Exception as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def login(self,nomusu,password):
        self.cursor.execute("SELECT clave FROM Usuarios WHERE nomusu='{0}'and clave='{1}' ".format(nomusu,password))
        if self.cursor.fetchall():
            messagebox.showinfo(title="Inicio de sesion correcto", message="Usuario y contraseña correcta, Bienvenido {0}".format(nomusu))
            return True
        else:
            messagebox.showinfo(title="Inicio de sesion incorrecto", message="Usuario y/o contraseña incorrecta")
            return False


#funcion encargada de cerrar la connexion con la DB
    def closeConnection(self):
        self.shopDB.close()
