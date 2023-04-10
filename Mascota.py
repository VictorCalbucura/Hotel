from datetime import date
import csv

class Mascota:
    def __init__(self, id, nombre, especie, raza, fecha_nacimiento, sexo, volumen):
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.volumen = volumen
        self.fichaMedica = list()

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_especie(self):
        return self.especie

    def get_raza(self):
        return self.raza

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def get_sexo(self):
        return self.sexo

    def get_volumen(self):
        return self.volumen
    
    ##Separación entre getters y setters
    
    def set_id(self, id):
        self.id = id

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_especie(self, especie):
        self.especie = especie

    def set_raza(self, raza):
        self.raza = raza

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def set_sexo(self, sexo):
        self.sexo = sexo

    def set_volumen(self, volumen):
        self.volumen = volumen

    def agregar_ficha(self, fichaMedica):
        self.fichaMedica.append(fichaMedica)

def cargar():
    id = input('Ingrese el id de la mascota: ')
    nombre = input('Ingrese nombre de la mascota: ')
    especie = input('Ingrese especie de la mascota: ')
    raza = input('Ingrese la raza de la mascota: ')
    fecha_nacimiento = input('Ingrese fecha de nacimiento de la mascota: ')
    sexo = input('Ingrese el sexo de la mascota: ')
    volumen = input('Ingrese el volumen de la mascota: ')

    mascota = Mascota(id, nombre, especie, raza, fecha_nacimiento, sexo, volumen)
    Mascotas.append(mascota)

Mascotas = []

cargar()

try:
    with open ('mascotas.csv', mode ='x', newline='') as file:
        escritor = csv.writer(file)
        escritor.writerow(["Id , Nombre , Especie , Raza , Fecha de Nacimiento , Sexo , Volumen"])
except FileExistsError:
        pass

def guardar():
    with open('mascotas.csv', mode='a', newline='') as file:
        for mascota in Mascotas:
            escritor = csv.writer(file)
            escritor.writerow([mascota.get_id(), mascota.get_nombre(), mascota.get_especie(), mascota.get_raza(), mascota.get_fecha_nacimiento(), mascota.get_sexo(), mascota.get_volumen()])

guardar()
