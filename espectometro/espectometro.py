import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Cargar el archivo de audio
audio_path = 'Audio.mp3'  # Cambia esto por la ruta de tu archivo de audio
y, sr = librosa.load(audio_path)

# Obtener el espectrograma de magnitud
S = np.abs(librosa.stft(y))

# Convertirlo a escala de decibelios (dB)
S_db = librosa.amplitude_to_db(S, ref=np.max)

# Visualizar el espectrograma
plt.figure(figsize=(10, 6))
librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de Voz')
plt.show()
