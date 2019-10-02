class Tipo:

#,question,question_type,options,answer
    def __init__(self,id_hecho,tipo,weighing):
        self.id_hecho= id_hecho
        self.tipo = tipo
        self.weighing = weighing

    #convierte un objeto de tipo Rule en un diccionario/documento
    def toDBCollection (self):
        return {
            "id_hecho": self.id_hecho,
            "tipo": self.tipo,
            "weighing": self.weighing
        }

    def __str__(self):
        return "weighing: %s " \
               %(self.weighing)