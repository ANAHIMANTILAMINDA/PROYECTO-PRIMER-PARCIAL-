class Estudiante:
    contador_estudiantes = 0

    def __init__(self, id, nivel):
        self._id = id
        self._nivel = nivel
        Estudiante.contador_estudiantes += 1

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, value):
        self._nivel = value

    def pedir_libro(self):
        # Lógica para solicitar un libro
        return True

    def devolver_libro(self):
        # Lógica para devolver un libro
        return True

# Ejemplo de uso
if __name__ == '__main__':
    estudiante1 = Estudiante(id=1, nivel=3)

    # Pedir un libro
    if estudiante1.pedir_libro():
        print(f"Estudiante {estudiante1.id} ha pedido un libro.")
    else:
        print(f"Estudiante {estudiante1.id} no pudo pedir el libro.")

    # Devolver un libro
    if estudiante1.devolver_libro():
        print(f"Estudiante {estudiante1.id} ha devuelto el libro.")
    else:
        print(f"Estudiante {estudiante1.id} no pudo devolver el libro.")
