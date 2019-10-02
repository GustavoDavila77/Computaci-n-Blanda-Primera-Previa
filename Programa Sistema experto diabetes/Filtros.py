class Filter:

    def __init__(self,description):
        self.description = description

    #convierte un objeto de tipo Filtro en un diccionario/documento
    def toDBCollection (self):
        return {
            "description":self.description,    
        }

    def __str__(self):
        return "Description: %s " \
               %(self.description)