#########################################
#---------Información General-----------#

#Tecnológico de Costa Rica
#Escuela de Electrónica

#Curso EL-5822 Taller de Instrumentación
#Prof. Kaleb Alfaro Badilla

# Laboratorio 1: Introducción a Taller de Instrumentación
# Parte 1: ANÁLISIS EN FRECUENCIA

#Elaborado por:
#-Alexander Castro Lara 2017153854
#-Andrés Carrillo Arroyo 2017106733
#-Kopper
#-Steven
#########################################


##########################################
#---------Librerías a utilizar-----------#
import numpy as np
import matplotlib.pyplot as plt 
from scipy.io import wavfile
import requests as req
from io import BytesIO
##########################################



###################################################
#---------Carga de las señales de audio-----------#

#Creación la variable con la URL de los datos
raw_wav_url_micro_1 = 'https://raw.githubusercontent.com/2017153854/Lab1_Taller/43b31a203f2045f209f52764331c40fe90895d6e/microA.wav'
raw_wav_url_micro_2 = 'https://raw.githubusercontent.com/2017153854/Lab1_Taller/43b31a203f2045f209f52764331c40fe90895d6e/microB.wav'

# Descarga de los audios de las URL
respuesta_micro_1 = req.get(raw_wav_url_micro_1)
respuesta_micro_2 = req.get(raw_wav_url_micro_2)
###################################################


###############################################################
#---------Acondicionamiento de las señales de audio-----------#
# Para poder trabajar las señales de audio con la librería NumPy
# es necesario convertirlas en una matriz de enteros 
# mediante "np.frombuffer" y "dtype=np.int16".

# Conversión a matriz de enteros
micro_1 = np.frombuffer(respuesta_micro_1.content, dtype=np.int16)
micro_2 = np.frombuffer(respuesta_micro_2.content, dtype=np.int16)
###############################################################



############################################
#---------Análisis en frecuencia-----------#
# Mediante "np.fft.fft()" se calcula la 
# transformada rápida de Fourier (espectro 
# de frecuencias) y con "np.abs()" su valor
# absoluta (espectro de magnitud)

# Calcula del espectro de magnitud
fft_micro_1 = np.abs(np.fft.fft(micro_1))
fft_micro_2 = np.abs(np.fft.fft(micro_2))
############################################



#####################################################
#---------Visualización de los resultados-----------#

# Frecuencias correspondientes a las transformadas:
# Antes de graficar, se debe calcular el rango de frecuancias.
# Para ello se utiliza "wavfile.read" para obtener la 
# frecuencia de muestreo y "np.fft.fftfreq" para 
# calcular las frecuencias correspondientes a los coeficientes de la FFT 
rango_muestreo_1, _ = wavfile.read(BytesIO(respuesta_micro_1.content))
frecuencias = np.fft.fftfreq(len(micro_1), d=1/rango_muestreo_1)

#Creación de la ventana de visualización
plt.figure()

#Grafica de los espectros de magnitud
plt.plot(frecuencias, fft_micro_1, label='Micrófono Celular') #Celular
plt.plot(frecuencias, fft_micro_2, label='Micrófono Computadora') #Computadora

#Acondicionamiento de las gráficas
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.title('Respuesta en Frecuencia de los Micrófonos')
plt.legend()
plt.grid()

#Acote de amplitud
plt.ylim(0, 100000000)

plt.show()
#####################################################






