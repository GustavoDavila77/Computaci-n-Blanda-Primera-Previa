from pymongo import MongoClient
from Filtros import Filter
from Fact import Fact

#filter
#1- 5d93da0d187f6d2fb4cc1eba
#2- 5d93da0d187f6d2fb4cc1ebb
#3- 5d93da0d187f6d2fb4cc1ebc
#4- 5d93da0d187f6d2fb4cc1ebd

# Creo una lista de objetos Ruta a insertar en la BD
filters = [Filter("sintoma"),Filter("antecedente"),Filter("enfermedades"),Filter("tipo diabetes")]

facts = [Fact("5d93da0d187f6d2fb4cc1eba","sed excesiva","¿Ha tenido sed excesiva?",1,['si','no']),
        Fact("5d93da0d187f6d2fb4cc1eba","micción frecuente","¿Tiene micción frecuente?",1,['si','no']),
        Fact("5d93da0d187f6d2fb4cc1eba","aumento del apetito","¿Ha tenido hambre excesiva?",1,['si','no']),
        Fact("5d93da0d187f6d2fb4cc1eba","fatiga","¿Se ha sentido fatigado?",1,['si','no']),
        Fact("5d93da0d187f6d2fb4cc1eba","visión borrosa","¿Ha tenido visión borrosa?",1,['si','no'])
        ]

#Conexión al Server de MongoDB Pasandole el host y el puerto
mongoClient = MongoClient('localhost',27017)


# Conexión a la base de datos --nombre db AsistenteRutas
db = mongoClient.DiabetesES

# Obtenemos una colecciones para trabajar con ellas
collection = db.filters

fact_collections = db.facts


# ingresamos los objetos rutas (o documentos en Mongo) en la coleccion filters
def fill_filter():
    try:
        for filter in filters:
            #convierte el objeto en colección
            obj = collection.insert_one(filter.toDBCollection())
            print('id de doc insert: '+ str(obj.inserted_id))
    except:
        print("imposible finished the process")
    
def fill_facts():
    try:
        for fact in facts:
            #convierte el objeto en colección
            obj = fact_collections.insert_one(fact.toDBCollection())
            print('id de doc insert: '+ str(obj.inserted_id))
    except ValueError:
        print("imposible to connect with database")
    

# PASO FINAL: Cerrar la conexion
mongoClient.close()
