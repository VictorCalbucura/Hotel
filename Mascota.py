class Mascota:
    def __init__(self, id, nombre, especie, raza, fecha_nacimiento, sexo, volumen)
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
