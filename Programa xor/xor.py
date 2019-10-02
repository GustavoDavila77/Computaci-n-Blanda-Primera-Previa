import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
 
# cargamos las 4 combinaciones de las compuertas XOR
training_data = np.array([[0,0],[0,1],[1,0],[1,1]], "float32")
 
# y estos son los resultados que se obtienen, en el mismo orden
target_data = np.array([[0],[1],[1],[0]], "float32")

#modelo vacio de tipo secuencial, serie de capas de neoronas secuenciales 
model = Sequential() 
#2 capas dense, una capa oculta con 16 neuronas, capa de entrada con 2 neuronas
#función de activación relu
model.add(Dense(16, input_dim=2, activation='relu')) 
model.add(Dense(1, activation='sigmoid')) #una capa con una neurona de salida
 

#antes de entrenar la red, se harán algunos ajustes
#tipo de perdida: la definimos para saber que tan lejos estamos de los valores a predecir
#el optimizador de los pesos de las conexiones de las neuronas
#metricas que vamos a optener
model.compile(loss='mean_squared_error',
              optimizer='adam',
              metrics=['binary_accuracy'])

#entrenamiento de la neurona
model.fit(training_data, target_data, epochs=1000)
 
# evaluamos el modelo
scores = model.evaluate(training_data, target_data)

#metrics and accuracy porcent
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
#Prediction results
print (model.predict(training_data).round())