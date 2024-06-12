from datetime import date

class Pedido:
    def __init__(self, id, solicitante, lista_material, materia, fecha_prestamo, fecha_devolucion, contador_pedido):
        self._id = id
        self._solicitante = solicitante
        self._lista_material = list()
        self._materia = materia
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion
        self._contador_pedido = contador_pedido

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        self._id = new_id

    @property
    def solicitante(self):
        return self._solicitante

    @solicitante.setter
    def solicitante(self, new_solicitante):
        self._solicitante = new_solicitante

    @property
    def lista_material(self):
        return self._lista_material

    @lista_material.setter
    def lista_material(self, new_lista_material):
        self._lista_material = new_lista_material

    @property
    def materia(self):
        return self._materia

    @materia.setter
    def materia(self, new_materia):
        self._materia = new_materia

    @property
    def fecha_prestamo(self):
        return self._fecha_prestamo

    @fecha_prestamo.setter
    def fecha_prestamo(self, new_fecha_prestamo):
        self._fecha_prestamo = new_fecha_prestamo

    @property
    def fecha_devolucion(self):
        return self._fecha_devolucion

    @fecha_devolucion.setter
    def fecha_devolucion(self, new_fecha_devolucion):
        self._fecha_devolucion = new_fecha_devolucion

    @property
    def contador_pedido(self):
        return self._contador_pedido

    @contador_pedido.setter
    def contador_pedido(self, new_contador_pedido):
        self._contador_pedido = new_contador_pedido

    def pedir_material(self, list_materia, solicitante, materia):
        # Lógica para solicitar material
        pass

    def devolver_material(self, solicitante):
        # Lógica para devolver material
        pass

# Ejemplo de uso
if __name__ == "__main__":
    pedido1 = Pedido(id=1, solicitante="estudiante", lista_material="libro", materia="Programacion orientada a objetos",
                     fecha_prestamo=date.today(), fecha_devolucion=None, contador_pedido=0)

    print(f"Pedido ID: {pedido1.id}")
    print(f"Solicitante: {pedido1.solicitante}")
    print(f"Material: {pedido1.lista_material}")
    print(f"Materia: {pedido1.materia}")
    print(f"Fecha de préstamo: {pedido1.fecha_prestamo}")
    print(f"Fecha de devolución: {pedido1.fecha_devolucion}")
    print(f"Contador de pedido: {pedido1.contador_pedido}")

