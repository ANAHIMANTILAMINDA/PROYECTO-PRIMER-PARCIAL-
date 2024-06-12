
from MATERIAL import Material
class Libro(Material):
    contador_libro = 0
    def __init__(self,codigo=None, autor=None, titulo=None, anio=2000, editorial=None, disponible=True, cantidad_disponible=0,tipo_pasta=None):
        Material.__init__(self, codigo= codigo,autor =autor,titulo=titulo,anio=anio,editorial=editorial,disponible=disponible,
                           cantidad_disponible = cantidad_disponible )
        self._tipo_pasta = tipo_pasta
        Libro.contador_libro += 1
        self._id_id =Libro.contador_libro
    @property
    def id(self):
     return self._id
    @property
    def tipo_pasta(self):
        return self._tipo_pasta
    @tipo_pasta.setter
    def tipo_pasta (self,valor):
        self._tipo_pasta= valor

    def __str__(self):
        return f'Libro{self.__dict__.__str__()}'
    def actualizar_disponibilidad(self,disponible):
        self.disponible=disponible
if __name__ == "__main__":
    l = Libro(codigo=1, autor='MANTILLA SALCEDO', titulo='100', editorial='ANAHI BRIGGITTE', anio=2024,
                 disponible=True, cantidad_disponible=5, tipo_pasta='MUY DURA')
    print(l)

