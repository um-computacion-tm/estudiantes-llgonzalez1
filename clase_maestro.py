from clase_persona import persona
class Profesor(persona):
    def __init__(self, param_nombre, param_apellido, param_email, param_numero):
        self.legajo_maestro= param_numero
        super().__init__(param_nombre, param_apellido, param_email)
profesor_persona_1= Profesor('Daniel', 'quinteros', 'dquinteros@gmail.com', 11211)
