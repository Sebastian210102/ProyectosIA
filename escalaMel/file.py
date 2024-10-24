import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


# Cargar el archivo de audio
senal, sr = librosa.load('Audio.mp3')

# Calcular el espectrograma de Mel
S = librosa.feature.melspectrogram(y=senal, sr=sr, n_mels=128)

# Convertir a escala logarítmica para mejor visualización
S_dB = librosa.power_to_db(S, ref=np.max)

# Visualizar el espectrograma de Mel
plt.figure(figsize=(10, 5))
librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel', cmap='viridis')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de Mel')
plt.show()
