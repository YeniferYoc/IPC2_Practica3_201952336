class Cliente:
    def __init__(self, nombre, dpi):#JAJA
        self.nombre = nombre
        self.dpi = dpi
        
    def getNombre(self):
        return self.nombre
    
    def getDpi(self):
        return self.dpi

    def mostrar_empresa(self):
        print("NOMBRE:  emp "+str(self.nombre)+" DPI:  "+str(self.dpi))
       