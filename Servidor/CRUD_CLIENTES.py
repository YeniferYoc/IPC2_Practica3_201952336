from ast import Str
from Cliente import *
class Crud_clientes():
    def __init__(self):
        self.clientes = []
    def AgregarCliente(self, dpi, nombre):
        self.clientes.append(Cliente(nombre,dpi))
        return 'CLIENTE AGREGADO'
    def MostrarTodos(self):
        retornar = ''
        for cliente in self.clientes:
            retornar += 'NOMBRE CLIENTE: '+str(cliente.nombre)+' DPI: '+str(cliente.dpi)
            retornar += '\n'
        return retornar
    def Actualizar_cliente(self, dpi, nombre):
        print(nombre)
        
        actualizado = False
        for cliente in self.clientes:
            dpi_cli = cliente.dpi
            if dpi_cli == dpi:
                cliente.nombre = nombre
                print(cliente.nombre)
                actualizado = True
        if actualizado == False:
            return 'NO SE PUDO ACTUALIZAR'
        else: 
            return 'ACTUALIZADO'
                
    def Borrar_cliente(self, dpi):
        eliminado = False
        for cliente in self.clientes:
            if cliente.dpi == dpi:
                self.clientes.remove(cliente)
                eliminado = True
        if eliminado == False:
            return 'NO SE PUDO ELIMINAR'
        else: 
            return 'CLIENTE ELIMINADO'

def main():
    clientes = Crud_clientes()
    clientes.AgregarCliente(1, 'yenifer')
    print(clientes.MostrarTodos())
if __name__ == "__main__":
    main()