class persona:
    def __init__(self, param_nombre, param_apellido, param_email):
        self.nombre= param_nombre
        self.apellido= param_apellido
        self.email= param_email
        self.asistencia= 0
    def registro_de_asistencia (self):
        self.asistencia += 1
persona_1= persona('marcos', 'cassone', 'mcassone@gmail.com')
