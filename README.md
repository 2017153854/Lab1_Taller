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

3. ¿Cómo afecta el ruido térmico al SNR de una señal analógica? ¿Cuántos dBm tiene el ruido térmico para una impedancia de 50Ω para una señal cuyo BW= 20kHz?
Dado que el ruido térmico es “el ruido debido al movimiento aleatorio de los electrones generado por la temperatura de los alrededores” [3], la forma en que afecta al SNR de una señal analógica es reduciendo su valor, pues la potencia del ruido aumenta. 
Para una impedancia de 50 Ω y un ancho de banda de 20 KHz, el nivel de ruido térmico, expresado en dBm (decibelios respecto a 1 miliwatio), se puede calcular realizando los siguientes pasos:
A.    Calcular la tensión RMS de ruido térmico (asumir 300 Kelvins como temperatura ambiente y k es la constante de boltzman) 
Vrms = √(4kTRΔf) = √[4(1.380649*10^-23 K/J)(300 K)(50 Ω)(20 KHz)] = 0.129 µV
B.    Luego, se debe calcular su respectiva potencia promedio en Watts
P ruido térmico (W) = [ (Vrms)^2 ] / R = [ (0.129 )^2 µV] / 50 Ω = 0.331*10^-15
C.    Por último, calcular la potencia de ruido térmico en dBm
P ruido térmico (dBm) = 10*log( P ruido térmico (W) / 1 mW ) = -124.8 dBm

5. ¿Para una grabación de audio, el piso de ruido de la señal es predominado por el ruido de cuantización o el ruido térmico?
En una grabación de audio, el piso de ruido de la señal suele estar predominado por el ruido de cuantización, especialmente cuando se utiliza una baja profundidad de bits por muestra (por ejemplo, 8 bits) en la digitalización. El ruido de cuantización es más evidente en señales de baja amplitud o en grabaciones con una relación señal-ruido (SNR) baja.

7. ¿Cuáles son las tasas de muestreo más populares para grabaciones de audio? ¿La cantidad de bits por muestra?
Las tasas de muestreo más populares para grabaciones de audio son 44.1 kHz, 48 kHz, 96 kHz y 192 kHz. La cantidad de bits por muestra, comúnmente conocida como resolución, suele ser de 16 bits o 24 bits. Tasas de muestreo más altas y una mayor resolución permiten una mayor calidad de audio y una reproducción más precisa de las señales analógicas originales.

9. ¿Cuáles son las tasas de muestreo más populares para grabaciones de audio? ¿La cantidad de bits por muestra?
Las tasas de muestreo más populares para grabaciones de audio son 44.1 kHz, 48 kHz, 96 kHz y 192 kHz. La cantidad de bits por muestra, comúnmente conocida como resolución, suele ser de 16 bits o 24 bits. Tasas de muestreo más altas y una mayor resolución permiten una mayor calidad de audio y una reproducción más precisa de las señales analógicas originales.

Harvey, D. (2022). 5.2: Fuentes de ruido instrumental. LibreTexts Español. https://espanol.libretexts.org/Quimica/Qu%C3%ADmica_Anal%C3%ADtica/An%C3%A1lisis_Instrumental_(LibreTextos)/05%3A_Se%C3%B1ales_y_Ruido/5.02%3A_Fuentes_de_Ruido_Instrumental
