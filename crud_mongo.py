from pymongo import MongoClient
from iniciar_db import fill_filter, fill_rules
from iniciar_db import fill_facts


#Conexión al Server de MongoDB Pasandole el host y el puerto
mongoClient = MongoClient('localhost',27017)

# Conexión a la base de datos 
db = mongoClient.DiabetesES

filter_collections = db.filters
facts_collections = db.facts

#update answer
def update_answer():
    pass


#User Questions
def questions():
    num_docs = facts_collections.count()
    print(num_docs)
    count = 0
    facts_pull = facts_collections.find()
    print(type(facts_pull))

    for f in facts_pull:
        print(f.get("question"))
        
        #si la pregunta es de si/no
        if f.get("question_type") == 1:
            op_array = f.get("options")

            for index in range(len(op_array)):
                print(str(index+1) +'.' + op_array[index])
            
            answer = int(input('R: '))
            
            if answer == 1:
                id_hecho= str(f.get("_id"))

            
        

#load, delete of collections
def load_filter():
  try:
    fill_filter()
    print('datos cargados a la colección')
  except:
    print('error al cargar datos a la colección')

def load_facts():
  try:
    fill_facts()
    print('datos cargados a la colección')
  except ValueError:
    print('error al cargar datos a la colección')

def load_rules():
  try:
    fill_rules()
    print('datos cargados a la colección')
  except ValueError:
    print('error al cargar datos a la colección')

def delete_filter():
  try:
    filter_collections.delete_many({})
    print('filter borrada')
  except:
    print('error al borrar filter')

def delete_facts():
  try:
    facts_collections.delete_many({})
    print('facts borrada')
  except:
    print('error al borrar facts')

###### Menu #######
#********************* cargar filter
#load_filter()

#********************* cargar hechos
#load_facts()

#********************* cargar rules
load_rules()

#**********************borrar filters
#delete_filter()

#**********************borrar facts
#delete_facts()
