from PERSONA import Persona

class Docente(Persona):
    contador_docente = 0

    def __init__(self, cedula=None, nombre=None, apellido=None, email=None, telefono=None, direccion=None, numero_libro=198, activo=3, carrera=None, id=1, titulo_3er_nivel=3, titulo_4to_nivel=4):
        super().__init__(cedula, nombre, apellido, email, telefono, direccion, numero_libro, activo, carrera)
        self._id = id
        self._titulo_3er_nivel = titulo_3er_nivel
        self._titulo_4to_nivel = titulo_4to_nivel
        Docente.contador_docente += 1

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def titulo_3er_nivel(self):
        return self._titulo_3er_nivel

    @titulo_3er_nivel.setter
    def titulo_3er_nivel(self, value):
        self._titulo_3er_nivel = value

    @property
    def titulo_4to_nivel(self):
        return self._titulo_4to_nivel

    @titulo_4to_nivel.setter
    def titulo_4to_nivel(self, value):
        self._titulo_4to_nivel = value

    def __str__(self):
        return f'Docente: {self.__dict__}'

    def pedir_libro(self):
        print(f"Docente {self.nombre} ha pedido un libro.")

    def devolver_libro(self):
        print(f"Docente {self.nombre} ha devuelto un libro.")

if __name__ == '__main__':
    d = Docente("2458741584", "monica", "morales", "monica@example.com", "09874563254154", "avenida quito", 198, 3, "matematica", 1, 3, 4)
    print(d)
    print(Docente.mro())
