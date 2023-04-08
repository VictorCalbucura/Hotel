from datetime import date

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

    def get_historiall(self, i):
        return self.historial[i]
    
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

    def set_email(self, newemail):
        self.email = newemail

    def set_telefono(self, newtelefono):
        self.telefono = newtelefono

    def set_domicilio(self, newdomicilio):
        self.domicilio = newdomicilio
    
    def set_mascotas(self, newmascotas, i):
        self.mascotas = newmascotas[i]

    def set_historial(self, newhistorial, i):
        self.historial = newhistorial[i]