
# Seleccionamos Tensorflow 2.0
try:
  # El comando %tensorflow_version solo existe en Colaboratory. Es un MAGIC COMMAND.
  %tensorflow_version 2.x
except Exception:
  pass
     

# Preparamos el entorno
import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
     

# Dataset de entrenamiento para puerta XOR
x_train = np.array([[0,0],[0,1],[1,0],[1,1]], dtype = "float32")
y_train = np.array([[0],[1],[1],[0]], dtype = "float32")
     

# Modelo MLP
model = keras.Sequential()
model.add(layers.Dense(2, input_dim = 2, activation = 'relu'))
model.add(layers.Dense(1, activation = 'sigmoid'))
     

# Comfiguracion del Modelo
model.compile(optimizer = keras.optimizers.Adam(0.01), loss='mean_squared_error', metrics = ['accuracy'])
     

# Entrenamiento
fit_history = model.fit(x_train, y_train, epochs = 400, batch_size = 1)
     

loss_curve = fit_history.history['loss']
accuracy_curve = fit_history.history['accuracy']
plt.plot(accuracy_curve, label = 'Precisión')
plt.plot(loss_curve, label = 'Perdida')
plt.legend(loc = 'lower left')
plt.title('Resultado del Entrenamiento')
plt.show
     

# Recuperamos bias and weights de la capa oculta
weights_HL, biases_HL = model.layers[0].get_weights()
# Recuperamos bias and weights de la capa de salida
weights_OL, biases_OL = model.layers[1].get_weights()
     

weights_HL, biases_HL
     

weights_OL, biases_OL