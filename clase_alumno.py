from clase_persona import persona
class alumno(persona):
    def __init__(self, param_nombre, param_apellido, param_email, param_legajo):
        self.legajo = param_legajo
        super().__init__(param_nombre, param_apellido, param_email)
alumno_persona_1= alumno('marcos', 'cassone', 'mcassone@gmail.com', 1111)
