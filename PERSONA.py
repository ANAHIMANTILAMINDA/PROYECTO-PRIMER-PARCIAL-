class Persona:
    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libro, activos, carrera):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._direccion = direccion
        self._numero_libro = numero_libro
        self._activos = activos
        self._carrera = carrera

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    @property
    def numero_libro(self):
        return self._numero_libro

    @numero_libro.setter
    def numero_libro(self, numero_libro):
        self._numero_libro = numero_libro

    @property
    def activos(self):
        return self._activos

    @activos.setter
    def activos(self, activos):
        self._activos = activos

    @property
    def carrera(self):
        return self._carrera

    @carrera.setter
    def carrera(self, carrera):
        self._carrera = carrera

    def __str__(self):
        return f'Persona {self.__dict__}'

if __name__ == '__main__':
    P = Persona(cedula='0965874584', nombre='BriggitteAnahy', apellido='MantillaSalcedo', email='anaman@hotmail.com',
                telefono='096587618', direccion='44 y la F', numero_libro='#9', activos='22', carrera='gig')
    print(P)
class Persona:
    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libro, activos, carrera):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._direccion = direccion
        self._numero_libro = numero_libro
        self._activos = activos
        self._carrera = carrera

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    @property
    def numero_libro(self):
        return self._numero_libro

    @numero_libro.setter
    def numero_libro(self, numero_libro):
        self._numero_libro = numero_libro

    @property
    def activos(self):
        return self._activos

    @activos.setter
    def activos(self, activos):
        self._activos = activos

    @property
    def carrera(self):
        return self._carrera

    @carrera.setter
    def carrera(self, carrera):
        self._carrera = carrera

    def __str__(self):
        return f'Persona {self.__dict__}'

if __name__ == '__main__':
    P = Persona(cedula='0965874584', nombre='BriggitteAnahy', apellido='MantillaSalcedo', email='anaman@hotmail.com',
                telefono='096587618', direccion='44 y la F', numero_libro='#9', activos='22', carrera='gig')
    print(P)
