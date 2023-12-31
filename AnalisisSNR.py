#########################################
#---------Información General-----------#

#Tecnológico de Costa Rica
#Escuela de Electrónica

#Curso EL-5822 Taller de Instrumentación
#Prof. Kaleb Alfaro Badilla

# Laboratorio 1: Introducción a Taller de Instrumentación
# Parte 2: CÁLCULO DEL SNR

#Elaborado por:
#-Alexander Castro Lara 2017153854
#-Andrés Carrillo Arroyo 2017106733
#-Douglas Kopper 2017220194
#-Steven Arias 2017097670
#########################################


##########################################
#---------LIBRERÍAS A UTILIZAR-----------#
import numpy as np
import matplotlib.pyplot as plt 
from scipy.io import wavfile
import requests as req
from io import BytesIO
##########################################



##########################################
#---------METODOLOGÍA-----------#
# 1. Cargar las grabaciones de los micrófonos (celular y laptop) desde archivos.
# 2. Cargar el tono de referencia de 1 kHz desde un archivo.
# 3. Definir un intervalo de tiempo en el que se encuentra el tono de referencia en las grabaciones.
# 4. Extraer las partes correspondientes de las grabaciones y del tono de referencia.
# 5. Calcular la potencia de la señal de referencia (tono de 1 kHz).
# 6. Para cada grabación de micrófono:
#     6.1 Calcular la potencia de la señal en el mismo intervalo de tiempo.
#     6.2 Calcular la relación señal-ruido (SNR) utilizando la potencia de la señal y la potencia del ruido.
# 9. Mostrar el valor del SNR para cada micrófono.
##########################################


# Crea la variable con la URL de los datos
raw_wav_url_micro_1 = 'https://raw.githubusercontent.com/2017153854/Lab1_Taller/43b31a203f2045f209f52764331c40fe90895d6e/microA.wav'
raw_wav_url_micro_2 = 'https://raw.githubusercontent.com/2017153854/Lab1_Taller/43b31a203f2045f209f52764331c40fe90895d6e/microB.wav'
raw_wav_url_reference = 'https://raw.githubusercontent.com/2017153854/Lab1_Taller/4a579e02c9deefe6864d587a7f7ab9352ffcf057/TonoDeReferencia1KHz.wav'

# Descargar los audios de las URL dadas
respuesta_micro_1 = req.get(raw_wav_url_micro_1)
respuesta_micro_2 = req.get(raw_wav_url_micro_2)
respuesta_reference = req.get(raw_wav_url_reference)

# Convierte los audios en señales para numpy (matriz de enteros de 16 bits)
micro_1 = np.frombuffer(respuesta_micro_1.content, dtype=np.int16)
micro_2 = np.frombuffer(respuesta_micro_2.content, dtype=np.int16)
reference = np.frombuffer(respuesta_reference.content, dtype=np.int16)

# Calcular la respuesta en frecuencia utilizando la transformada rápida de Fourier
fft_micro_1 = np.abs(np.fft.fft(micro_1))
fft_micro_2 = np.abs(np.fft.fft(micro_2))
fft_reference = np.abs(np.fft.fft(reference))

# Frecuencias correspondientes a las transformadas
rango_muestreo_1, _ = wavfile.read(BytesIO(respuesta_micro_1.content))
frecuencias = np.fft.fftfreq(len(micro_1), d=1/rango_muestreo_1)

# Buscar la frecuencia más cercana a 1 kHz en las frecuencias
reference_frequency_index = np.argmin(np.abs(frecuencias - 1000))
reference_amplitude = fft_reference[reference_frequency_index]

# Calcular el SNR para cada micrófono
snr_micro_1 = fft_micro_1[reference_frequency_index] / reference_amplitude
snr_micro_2 = fft_micro_2[reference_frequency_index] / reference_amplitude

#Visualización de resultados
print("SNR Microfono Celular:", snr_micro_1)
print("SNR Microfono Computadora:", snr_micro_2)





