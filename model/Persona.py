class Persona:
    def __init__(self, nombre='', cantidadPersonas=0, cantidadBoletos=0):
        self.nombre = nombre
        self.cantidadPersonas = cantidadPersonas
        self.cantidadBoletos = cantidadBoletos
    def crearPersona(self, nombre, personas, boletos):
        self.nombre = nombre
        self.cantidadPersonas = personas
        self.cantidadBoletos = boletos
        print(f'{self.nombre}')
    def calcularPrecio(self,personas, boletos):
        self.total =  12.0 * boletos
        return round(self.total, 2)
    def verificar(self):
        
        limite = self.cantidadPersonas * 7
        if self.cantidadBoletos > limite:
            return False
        else:
            return True
        
    def descuento(self):
        if self.cantidadBoletos > 5:
            descuento = self.total * 0.15
            return round(self.total - descuento, 2)
        elif self.cantidadBoletos == 3 or self.cantidadBoletos == 4 or self.cantidadBoletos == 5:
            descuento = self.total * 0.10
            return round(self.total - descuento, 2)
        else:
            return self.total
    def tarjetaDescuento(self, total):
        descuento = total * 0.10
        total = total - descuento
        return round(total, 2)
    
    def verificarDatos(self):
        if self.cantidadPersonas <= 0 or self.cantidadBoletos <= 0 or self.nombre.strip() == '':
            return False
        else:
            return True