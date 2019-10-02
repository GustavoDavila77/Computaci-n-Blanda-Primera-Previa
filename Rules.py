class Rule:

#,question,question_type,options,answer
    def __init__(self,antecedent, consecuent,weighing):
        self.antecedent = antecedent
        self.consecuent = consecuent
        self.weighing = weighing

    #convierte un objeto de tipo Rule en un diccionario/documento
    def toDBCollection (self):
        return {
            "antecedent": self.antecedent,
            "consecuent": self.consecuent,
            "weighing": self.weighing
        }

    def __str__(self):
        return "weighing: %s " \
               %(self.weighing)