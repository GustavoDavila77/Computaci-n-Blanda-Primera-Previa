from pymongo import MongoClient
from iniciar_db import fill_filter, fill_rules, fill_tipos
from iniciar_db import fill_facts
from Agendas import Agenda


#Conexión al Server de MongoDB Pasandole el host y el puerto
mongoClient = MongoClient('localhost',27017)

# Conexión a la base de datos 
db = mongoClient.DiabetesES

filter_collections = db.filters
facts_collections = db.facts
rules_collections = db.rules
agenda_collections = db.agenda
tipos_collections = db.tipos

#update weighing/ponderación
def update_weighing():
  pass

def consecuent_tipos(id_rule,weighind):
  tipos = tipos_collections.find()
  for t in tipos:
    if t.get('weighing') == 0:
      agenda_insert(id_rule,weighind)
    elif t.get('weighing') > 0:
      print('actualizar peso')

#update answer
#busco en los antecedentes de las reglas si esta ese id
def update_answer(id_hecho):
  #encuentra todos los antecedentes con el id_hecho
  rule_cursor = rules_collections.find({"antecedent":{"$in":[id_hecho]}})

  for rule in rule_cursor:
    id_rule = rule['_id']
    weighing = rule['weighing']
    consecuent = rule['consecuent']
    print('id_rule: '+ str(rule['_id']))

    #si la coleccion esta vacia
    if agenda_collections.count() == 0:
      agenda_insert(id_rule,weighing)
      print('inserto agende 1era vez')

    elif agenda_collections.count() > 0:
      #mirar si el consecuente ya se encuentra en id de tipos -- ponderacion = 0.0
      con_consecuent = consecuent_tipos(id_rule,weighing)
        

def agenda_insert(id_rule,weighing):
  agen = Agenda(id_rule,weighing)
  db.agenda.insert_one(agen.toDBCollection())
  print('se inserto agenda')

#User Questions
def questions():
    num_docs = facts_collections.count()
    print(num_docs)
    con1 = 0
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
                #print('id_hecho: '+ id_hecho)
                update_answer(id_hecho)
                con1 = con1 +1
    
    print(prob(con1))

            
        

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

def load_tipos():
  try:
    fill_tipos()
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

#probabilidades basadas en el test de findrics
def prob(con1):
  if con1 == 0:
    p= 0
  elif con1 == 2:
    p = 0.2
  elif con1 == 3:
    p= 0.5
  elif con1 >= 5:
    p = 0.7
  else:
    print('ingrese un valor valido')

  return 'la probabilidad es de: ' + str(p)

def reset_agenda():
  try:
    agenda_collections.delete_many({})
    print('agenda borrada')
  except:
    print('error al borrar facts')

###### Menu #######
#********************* cargar filter
#load_filter()

#********************* cargar hechos
#load_facts()

#********************* cargar rules
#load_rules()

#********************* cargar tipos
#load_tipos()
#**********************borrar filters
#delete_filter()

#**********************borrar facts
#delete_facts()
