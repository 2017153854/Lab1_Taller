import numpy as np
import matplotlib.pyplot as plt 
from scipy.io import wavfile
import requests as req
from io import BytesIO

# Crea la variable con la URL de los datos
raw_wav_url_micro_1 = 'https://raw.githubusercontent.com/2017153854/Lab1_Taller/43b31a203f2045f209f52764331c40fe90895d6e/microA.wav'
raw_wav_url_micro_2 = 'https://raw.githubusercontent.com/2017153854/Lab1_Taller/43b31a203f2045f209f52764331c40fe90895d6e/microB.wav'

# Descargar los audios de las URL dadas
respuesta_micro_1 = req.get(raw_wav_url_micro_1)
respuesta_micro_2 = req.get(raw_wav_url_micro_2)

# Convierte los audios en señales para  numpy
micro_1 = np.frombuffer(respuesta_micro_1.content, dtype=np.int16)
micro_2 = np.frombuffer(respuesta_micro_2.content, dtype=np.int16)

# Calcular la respuesta en frecuencia utilizando la transformada rapida de Fourier
fft_micro_1 = np.abs(np.fft.fft(micro_1))
fft_micro_2 = np.abs(np.fft.fft(micro_2))

# Frecuencias correspondientes a las transformadas
rango_muestreo_1, _ = wavfile.read(BytesIO(respuesta_micro_1.content))
frecuencias = np.fft.fftfreq(len(micro_1), d=1/rango_muestreo_1)

# Visualizar los resultados
plt.figure()
plt.plot(frecuencias, fft_micro_1, label='Micrófono Celular') #Celular
plt.plot(frecuencias, fft_micro_2, label='Micrófono Computadora') #Computadora
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.title('Respuesta en Frecuencia de los Micrófonos')
plt.legend()
plt.grid()
plt.ylim(0, 100000000)
plt.show()







