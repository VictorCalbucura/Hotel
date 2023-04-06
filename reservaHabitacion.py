class ReservaHabitacion:
    def __init__(self, idReserva, tipoMascota, tamMascota, habitacionSel, fechaEnt):
        self.idReserva = idReserva
        self.tipoMascota = tipoMascota
        self.tamMascota = tamMascota
        self.habitacionSel = habitacionSel
        self.fechaEnt = fechaEnt
        self.historial = []
    
    def agendarReserva(self):
        self.historial.append(self)
    
    def modificarReserva(self, newHabitacionSel, newFechaEnt):
        self.habitacionSel = newHabitacionSel
        self.fechaEnt = newFechaEnt
    
    def calcular_precio(self, hab, dias, tam, cantMasc):
        prHab = 0
        if hab == "simple":
            prHab = 6000
        elif hab == "amplia":
            prHab = 7000
        elif hab == "suite":
            prHab = 8500
        prTam = 0
        if tam == "muy pequeño":
            prTam = 2000
        elif tam == "pequeño":
            prTam = 2500
        elif tam == "mediano":
            prTam = 3500
        elif tam == "grande":
            prTam = 5500
        elif tam == "muy grande":
            prTam = 8000
        descDias = 0
        if dias > 7:
            descDias = 0.3
        descMasc = 0
        if cantMasc > 1:
            descMasc = 0.4
        precio = ((prHab + prTam)*dias) - ((dias*prHab*descDias) + (dias*prTam*descMasc))
        return precio
    
    def ver_historial_reservas(self):
        for reserva in self.historial:
            print("ID de Reserva: " + reserva.idReserva)
            print("Tipo de Mascota: " + reserva.tipoMascota)
            print("Tamaño de Mascota: " + reserva.tamMascota)
            print("Habitación Seleccionada: " + reserva.habitacionSel)
    
    def cancelar_reserva(self, idReserva):
        for reserva in self.historial:
            if reserva.idReserva == idReserva:
                self.historial.remove(reserva)
                print("La reserva con ID " + idReserva + " ha sido cancelada.")
                return
        print("No se encontró la reserva con ID " + idReserva + ".")