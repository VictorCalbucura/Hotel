class disponibilidadHorario:
    def __init__(self, horarioDisponible, horarioOcupado):
        self.horarioDisponible = horarioDisponible
        self.horarioOcupado = horarioOcupado
    
    def setHorarioDisponible(self, fechaD):
        self.horarioDisponible = fechaD
        
    def setHorarioOcupado(self, fechaO):
        self.horarioOcupado = fechaO