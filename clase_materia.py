from clase_alumno import alumno
class materia(alumno):
    def __init__(self,  param_nombre, param_apellido, param_email, param_legajo):
        self.lista= []
        super().__init__( param_nombre, param_apellido, param_email, param_legajo)
    def agregar_materia(self, materia):
        self.lista.append(materia)

materia_alumno_persona_1= materia('marcos', 'cassone', 'mcassone@gmail.com', 1111)
