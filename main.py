from Pedido import Pedido
from Estudiante import Estudiante
from Libro import Libro


estudiante1 = Estudiante(cedula='0950465757', nombre='ANAHI', apellido='Mantilla', nivel='3')
estudiante2 = Estudiante(cedula='0996789659', nombre='Briggitte', apellido='SALCEDO', nivel='3')


l1 = Libro(codigo='1206', autor='magia', titulo='super', editorial='AM', anio='2003',
           disponible=True, cantidad_disponible=4, tipo_pasta='dura')
l2 = Libro(codigo='2216', autor='LINDA', titulo='LUNA', editorial='BS', anio='2004',
           disponible=True, cantidad_disponible=3, tipo_pasta='Blanda')

lista_materiales = [l1, l2]


pedido1 = Pedido()
pedido1.pedir_material(materia='PROGRAMACION ORIENTADA A OBJETOS', solicitantes=estudiante1, lista_materiales=lista_materiales)
print(pedido1)
print(pedido1.mostrar_materiales())
