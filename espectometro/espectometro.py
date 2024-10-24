import librosa                      # análisis de audio y música
import librosa.display              # visualizaciones específicas (espectrogramas, etc.)
import matplotlib.pyplot as plt     # para trazar datos y visualizaciones de audio
import numpy as np                  # para trabajar con arrays numéricos

def seleccionarAudio():             
    opc = int(input("Selecciona el audio:\n1. Prueba2\n2. Ninguno\n>>> "))
    if opc == 1:
        miAudio = 'Audio.mp3'
    elif opc == 2:
        miAudio = ''
    else:
        print("Opción no válida. Usando audio por defecto.")
        miAudio = 'audios/prueba2.mp3'
    return miAudio

def main():
    miAudio = seleccionarAudio()
    
    # Verificar si se seleccionó un archivo
    if miAudio == '':
        print("No se ha seleccionado un archivo de audio.")
        return

    # Cargamos el audio a analizar
    try:
        senal, sr = librosa.load(miAudio)
        print(f"Audio cargado correctamente: {miAudio}")
    except Exception as e:
        print(f"Error al cargar el audio: {e}")
        return
    
    # Indica la cantidad de muestras (samples)
    print(f"Forma de la señal de audio: {senal.shape}")

    # EXTRACCIÓN DE MFCCs
    mfcc = librosa.feature.mfcc(y=senal, n_mfcc=13, sr=sr)

    # Visualización de los coeficientes
    plt.figure(figsize=(25,10))
    librosa.display.specshow(mfcc, x_axis="time", sr=sr)
    plt.colorbar(format="%+2f")
    plt.title("Coeficientes MFCC")
    plt.show()

# Ejecutar el programa
main()

