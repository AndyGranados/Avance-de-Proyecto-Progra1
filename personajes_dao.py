# -*- coding: utf-8 -*-
from conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()
    
    sql = '''
    CREATE TABLE personajes(
        id_personajes INTEGER,
        nombre VARCHAR(100),
        franquicia VARCHAR(100),
        poder_principal VARCHAR(100),
        PRIMARY KEY (id_personajes AUTOINCREMENT)
    )'''
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Craer Registro'
        mensaje = 'Se creo la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'La tabla ya esta creada'
        messagebox.showwarning(titulo, mensaje)
        

def borrar_tabla():
    conexion = ConexionDB()
    
    sql = 'DROP TABLE personajes'
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar Registro'
        mensaje = 'La tabla de la base de datos se borro con éxito'
        messagebox.showinfo(titulo, mensaje)
    except: 
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar Registro'
        mensaje = 'No hay tabla para borrar'
        messagebox.showerror(titulo, mensaje)
        
class Personajes:
    def __init__(self, nombre, franquicia, poder_principal):
        self.id_personajes = None
        self.nombre = nombre
        self.franquicia = franquicia
        self.poder_principal = poder_principal
    
    def __str__(self):
        return f'Personajes[{self.nombre},{self.franquicia},{self.poder_principal}]'
        
def guardar(personajes):
    conexion = ConexionDB()
    
    sql = f"""INSERT INTO personajes (nombre, franquicia, poder_principal)
    VALUES('{personajes.nombre}','{personajes.franquicia}','{personajes.poder_principal}')"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Conexion  al Registro'
        mensaje = 'La tabla personajes no esta creado en la base de datos'
        messagebox.showerror(titulo, mensaje)

def listar():
    conexion = ConexionDB()
    
    lista_personajes = []
    sql = 'SELECT * FROM personajes'
    
    try:
        conexion.cursor.execute(sql)
        lista_personajes = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'Crea la tabla en la base datos'
        messagebox.showwarning(titulo, mensaje)
        
    return lista_personajes

def editar(personajes, id_personajes):
    conexion = ConexionDB()
    
    sql = f"""UPDATE personajes
    SET nombre = '{personajes.nombre}', franquicia = '{personajes.franquicia}',
    poder_principal = '{personajes.poder_principal}'
    WHERE id_personajes = {id_personajes}"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Edición de datos'
        mensaje = 'No se ha podido editar este registro'
        messagebox.showerror(titulo, mensaje)
        
def eliminar(id_personajes):
    conexion = ConexionDB()
    
    sql = f'DELETE FROM personajes WHERE id_personajes = {id_personajes}'
    
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Eliminar datos'
        mensaje = 'No se pudo eliminar el registro'
        messagebox.showerror(titulo, mensaje)
        
    
        
        
        
        