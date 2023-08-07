# Lab1_Taller
Laboratorio 1 del curso EL-5822 Taller de Instrumentación


Cuestionario Previo

A continuación, se en listan las preguntas con sus respectivas respuestas:

1. ¿Cómo se mide el signal-to-noise ratio (SNR) para una señal analógica? Brinde un ejemplo.
Dado que la Signal-to-Noise Ratio (SNR) es “la proporción existente entre la potencia de la señal de referencia o en estudio y la potencia del ruido que la corrompe” [1], entonces por definición la manera de calcularla será haciendo una medición de la potencia de la señal que nos interesa, para posterior a ello dividirla entre la potencia del ruido presente. Asimismo, la SNR es una cantidad expresada generalmente en decibelios (dB), por lo que la fórmula completa queda de la siguiente manera:
SNR (dB) = 10 * log10(Potencia de la señal / Potencia del ruido)
Ejemplo: Si se determinase en el laboratorio que una señal analógica cuenta con una potencia de 1 W y que la potencia del ruido es de 0.01 W, el SNR sería:
SNR (dB) = 10 * log10(1 W / 0.01 W) = 10 * log10(100) = 20 dB
https://recursoinformatico.weebly.com/uploads/1/0/7/3/107381475/snr.pdf

2. ¿Cuál es el ancho de banda típico para señales de audio? ¿Una señal de audio tiene componente DC?
El ancho de banda típico de una señal de audio corresponde al rango de frecuencias perceptibles para el oído humano, es decir, “el intervalo de frecuencias de 20 a 20,000 Hz, llamado gama audible” [2]. En relación con la componente DC, las señales de audio, por lo general, no tiene una componente DC significativa, ya que están diseñadas para transmitir la información sin una componente de corriente continua.
W. Sears, M.W. Zemansky, H.D. Young y R.A. Freedman. (2009). Física Universitaria. 12Ed. Vol 1. Pearson Education
