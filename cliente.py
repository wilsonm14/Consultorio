class Cliente:

    def __init__(self, cedula, nombre, telefono, tipo_cliente, tipo_atencion, cantidad, prioridad_atencion, fecha_cita):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.tipo_cliente = str(tipo_cliente).lower()
        self.tipo_atencion = str(tipo_atencion).lower()
        self.prioridad_atencion = prioridad_atencion
        self.fecha_cita = fecha_cita

        if self.tipo_atencion in ["limpieza", "diagnostico"]:
            self.cantidad = 1
        elif self.tipo_atencion in ["calzas", "extraccion"]:
            if cantidad >= 1:
                self.cantidad = cantidad
            else:
                self.cantidad = 1
        else:
            self.cantidad = 1

        self.val_cita = self.valor_cita()
        self.val_atencion = self.valor_atencion() * self.cantidad
        self.total_pagar = self.val_cita + self.val_atencion

    def valor_cita(self):
        if self.tipo_cliente == "particular":
            return 80000
        elif self.tipo_cliente == "eps":
            return 5000
        elif self.tipo_cliente == "prepagada":
            return 30000
        else:
            return 0

    def valor_atencion(self):
        if self.tipo_cliente == "particular":
            if self.tipo_atencion == "limpieza":
                return 60000
            elif self.tipo_atencion == "calzas":
                return 80000
            elif self.tipo_atencion == "extraccion":
                return 100000
            elif self.tipo_atencion == "diagnostico":
                return 50000

        elif self.tipo_cliente == "eps":
            if self.tipo_atencion == "limpieza":
                return 0
            elif self.tipo_atencion == "calzas":
                return 40000
            elif self.tipo_atencion == "extraccion":
                return 40000
            elif self.tipo_atencion == "diagnostico":
                return 0

        elif self.tipo_cliente == "prepagada":
            if self.tipo_atencion == "limpieza":
                return 0
            elif self.tipo_atencion == "calzas":
                return 10000
            elif self.tipo_atencion == "extraccion":
                return 10000
            elif self.tipo_atencion == "diagnostico":
                return 0
        return 0

    def mostrar_informacion(self):
        print(f"Cedula: {self.cedula} - Nombre: {self.nombre} - Telefono: {self.telefono} - Tipo Cliente: {self.tipo_cliente} - Atencion: {self.tipo_atencion} (Cantidad: {self.cantidad}) - Prioridad: {self.prioridad_atencion} - Fecha Cita: {self.fecha_cita} - Valor Cita: ${self.val_cita} - Valor Atencion: ${self.val_atencion} - Total a pagar: ${self.total_pagar}")