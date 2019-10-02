class Agenda:

#,question,question_type,options,answer
    def __init__(self,id_rule,weighing):
        self.id_rule = id_rule
        self.weighing = weighing

    #convierte un objeto de tipo Rule en un diccionario/documento
    def toDBCollection (self):
        return {
            "id_rule": self.id_rule,
            "weighing": self.weighing
        }

    def __str__(self):
        return "weighing: %s " \
               %(self.weighing)