from datetime import date
import csv

class Usuario:
    def __init__(self, id, nombre, apellido_paterno, apellido_materno, genero, fecha_nacimiento, rut):
        self.id = id
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.genero = genero
        self.fecha_nacimiento = fecha_nacimiento
        self.rut = rut
        self.cargo = list()

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
    
    def get_cargo(self):
        return self.cargo

##Separación entre getters y setters
    
    def set_id(self, newid):
        self.id = newid

    def set_nombre(self, newnombre):
        self.nombre = newnombre
    
    def set_apellido_paterno(self, newapellido_paterno):
        self.apellido_paterno = newapellido_paterno
    
    def set_apellido_materno(self, newapellido_materno):
        self.apellido_materno = newapellido_materno

    def set_genero(self, newgenero):
        self.genero = newgenero

    def set_fecha_nacimiento(self, newfecha_nacimiento):
        self.fecha_nacimiento = newfecha_nacimiento

    def set_rut(self, newrut):
        self.rut = newrut

    def agregar_cargo(self, cargo):
        self.cargo.append(cargo)

    
def cargar():
    id = input('Ingrese su id: ')
    nombre = input('Ingrese su nombre: ')
    apellido_paterno = input('Ingrese su apellido paterno: ')
    apellido_materno = input('Ingrese su apellido materno: ')
    genero = input('Ingrese su genero: ')
    fecha_nacimiento = input('Ingrese su fecha de nacimiento: ')
    rut = input('Ingrese su rut: ')

    usuario = Usuario(id, nombre, apellido_paterno, apellido_materno, genero, fecha_nacimiento, rut)
    Usuarios.append(usuario)
    
Usuarios = []

cargar()

try:
    with open ('usuarios.csv', mode ='x', newline='') as file:
        escritor = csv.writer(file)
        escritor.writerow(["Id , Nombre , Apellido Paterno , Apellido Materno , Genero , Fecha de nacimiento, Rut"])
except FileExistsError:
        pass

def guardar():
    with open('usuarios.csv', mode='a', newline='') as file:
        for usuario in Usuarios:
            escritor = csv.writer(file)
            escritor.writerow([usuario.get_id(), usuario.get_nombre(), usuario.get_apellido_paterno(), usuario.get_apellido_materno(), usuario.get_genero(), usuario.get_fecha_nacimiento(), usuario.get_rut()])

guardar()