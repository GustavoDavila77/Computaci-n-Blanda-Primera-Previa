class Fact:

#,question,question_type,options,answer
    def __init__(self,id_filtro,description,question,question_type,options):
        self.id_filtro = id_filtro
        self.description = description
        self.question = question
        self.question_type = question_type
        self.options = options

    #convierte un objeto de tipo Filtro en un diccionario/documento
    def toDBCollection (self):
        return {
            "id_filtro": self.id_filtro,
            "description":self.description, 
            "question" : self.question,
            "question_type": self.question_type,
            "options": self.options
        }

    def __str__(self):
        return "Description: %s " \
               %(self.description)