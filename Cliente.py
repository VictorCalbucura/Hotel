from datetime import date
import csv

class Cliente:
    def __init__(self, id, nombre, apellido_paterno, apellido_materno, genero, fecha_nacimiento, rut, email, telefono, domicilio):
        self.id = id
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.genero = genero
        self.fecha_nacimiento = fecha_nacimiento
        self.rut = rut
        self.email = email
        self.telefono = telefono
        self.domicilio = domicilio
        self.mascotas = list()
        self.historial = list()


    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_apellido_paterno(self):
        return self.apellido_paterno

    def get_apellido_materno(self):
        return self.apellido_materno

    def get_genero(self):
        return self.genero

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def get_rut(self):
        return self.rut

    def get_email(self):
        return self.email

    def get_telefono(self):
        return self.telefono

    def get_domicilio(self):
        return self.domicilio

    def get_mascotas(self):
        return self.mascotas
    
    def get_mascota(self, i):
        return self.mascotas[i]

    def get_historial(self):
        return self.historial

    ##Separación entre getters y setters
    
    def set_id(self, id):
        self.id = id

    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_apellido_paterno(self, apellido_paterno):
        self.apellido_paterno = apellido_paterno
    
    def set_apellido_materno(self, apellido_materno):
        self.apellido_materno = apellido_materno

    def set_genero(self, genero):
        self.genero = genero

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def set_rut(self, rut):
        self.rut = rut

    def set_email(self, email):
        self.email = email

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_domicilio(self, domicilio):
        self.domicilio = domicilio
    
    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def agregar_historial(self, historial):
        self.historial.append(historial)

def cargar():
    id = input('Ingrese el id: ')
    nombre = input('Ingrese el nombre: ')
    apellido_paterno = input('Ingrese el apellido paterno: ')
    apellido_materno = input('Ingrese el apellido materno: ')
    genero = input('Ingrese su genero: ')
    fecha_nacimiento = input('Ingrese su fecha de nacimiento: ')
    rut = input('Ingrese su rut: ')
    email = input('Ingrese su email: ')
    telefono = input('Ingrese su teléfono: ')
    domicilio = input('Ingrese su domicilio: ')

    cliente = Cliente(id, nombre, apellido_paterno, apellido_materno, genero, fecha_nacimiento, rut, email, telefono, domicilio)
    Clientes.append(cliente)

Clientes = []

cargar()

try:
    with open ('clientes.csv', mode ='x', newline='') as file:
        escritor = csv.writer(file)
        escritor.writerow(["Id , Nombre , Apellido Paterno , Apellido Materno , Genero , Fecha de nacimiento , Email, Rut , Telefono , Domicilio "])
except FileExistsError:
        pass

def guardar():
    with open('clientes.csv', mode='a', newline='') as file:
        for cliente in Clientes:
            escritor = csv.writer(file)
            escritor.writerow([cliente.get_id(), cliente.get_nombre(), cliente.get_apellido_paterno(), cliente.get_apellido_materno(), cliente.get_genero(), cliente.get_fecha_nacimiento(), cliente.get_rut(), cliente.get_email(), cliente.get_telefono(), cliente.get_domicilio()])

guardar()

