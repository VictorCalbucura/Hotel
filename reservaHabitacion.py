class ReservaHabitacion:
    def __init__(self, idReserva, tipoMascota, tamMascota, habitacionSel, fechaEnt, cantMasc):
        self.idReserva = idReserva
        self.tipoMascota = tipoMascota
        self.tamMascota = tamMascota
        self.habitacionSel = habitacionSel
        self.fechaEnt = fechaEnt
        self.cantMasc = cantMasc
        self.mascRes = []
        self.historial = []
        self.precio = 0
    
    def agendarReserva(self):
        self.historial.append(self)
    
    def modificarReserva(self, newHabitacionSel, newFechaEnt, newCantMasc):
        self.habitacionSel = newHabitacionSel
        self.fechaEnt = newFechaEnt
        self.cantMasc = newCantMasc
    
    def calcular_precio(self, dias):
        prHab = 0
        if self.habitacionSel == "simple":
            prHab = 6000
        elif self.habitacionSel == "amplia":
            prHab = 7000
        elif self.habitacionSel == "suite":
            prHab = 8500
        prTam = 0
        if self.tamMascota == "muy pequeño":
            prTam = 2000
        elif self.tamMascota == "pequeño":
            prTam = 2500
        elif self.tamMascota == "mediano":
            prTam = 3500
        elif self.tamMascota == "grande":
            prTam = 5500
        elif self.tamMascota == "muy grande":
            prTam = 8000
        descDias = 0
        if dias > 7:
            descDias = 0.3
        descMasc = 0
        if self.cantMasc > 1:
            descMasc = 0.4
        self.precio = ((prHab + prTam)*dias) - ((dias*prHab*descDias) + (dias*prTam*descMasc))
        return self.precio
    
    def ver_historial_reservas(self):
        for reserva in self.historial:
            print("ID de Reserva: " + str(reserva.idReserva))
            print("Tipo de Mascota: " + str(reserva.tipoMascota))
            print("Tamaño de Mascota: " + str(reserva.tamMascota))
            print("Habitación Seleccionada: " + str(reserva.habitacionSel))
    
    def cancelar_reserva(self, idReserva):
        for reserva in self.historial:
            if reserva.idReserva == idReserva:
                self.historial.remove(reserva)
                print("La reserva con ID " + str(idReserva) + " ha sido cancelada.")
                return
        print("No se encontró la reserva con ID " + str(idReserva) + ".")