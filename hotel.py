class ReservaHabitacion:
    def __init__(self):
        self.habitaciones = []
        self.reservas = []
        
    def registrarHabitaciones(self):
        self.habitaciones.append(self)
        
    def registrarReservas(self):
        self.reservas.append(self)
        
    def habitacionOcupada(self, hab):
        hab = 0
        return hab
    
    def habitacionDesocupada(self, hab):
        hab = 1
        return hab
    
    def CheckIn(self, habitacion):
        self.habitacionOcupada(self.habitaciones(habitacion))
        
    def CheckOut(self, habitacion):
        self.habitacionOcupada(self.habitaciones(habitacion))
        
    def buscarHabitacionDisponible(self):
        for habitaciones in self.habitaciones:
            if habitaciones.habitacion == 0:
                print("La habitacion " + habitaciones.habitacion + " esta desocupada")
            
        