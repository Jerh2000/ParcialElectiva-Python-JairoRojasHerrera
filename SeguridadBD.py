import sqlite3
from tkinter import messagebox

class Seguridad:
    
    def abrir(self):
        conexion=sqlite3.connect("BaseDatos.db")
        return conexion

    def agregar(self,datos):
        try:
            conexion = self.abrir()
            cursor = conexion.cursor()
            sql="insert into Registros(Id,Nombres,Apellidos,Salud,Pension,RiesgosL,CajaC) values(?,?,?,?,?,?,?)"
            cursor.execute(sql,datos)
            conexion.commit()
            conexion.close()
            return True
        except:
            messagebox.showwarning("Numero registrado","Ya has registrado un contacto con ese numero");
            return False
            
    def ConsultarR(self,ide):
        try:
            conexion = self.abrir()
            cursor = conexion.cursor()
            sql="select * from Registros where Id=?"
            cursor.execute(sql,ide)
            return cursor.fetchall()
        finally:
            conexion.close()
            
    def ListarRegistros(self):
        try:
            conexion = self.abrir()
            cursor = conexion.cursor()
            sql="select * from Registros"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            conexion.close()
            
    def ActualizarRegistro(self,datos,ide):
        try:
            conexion = self.abrir()
            cursor = conexion.cursor()
            sql = (f"update Registros set Id=?,Nombres=?,Apellidos=?,Salud=?,Pension=?,RiesgosL=?,CajaC=? where Id={ide}")
            cursor.execute(sql,datos)
            conexion.commit()
            return True
        except:
            conexion.close()
            messagebox.showwarning("Ya existe un registro","Ya hay un registro con ese numero de identificacion");