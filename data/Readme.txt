https://www.kaggle.com/fournierp/captcha-version-2-images/downloads/captcha-version-2-images.zip/2

Datos obtenidos de la url indicada. 

1) Se transforman todas las imagenes a jpg con el siguiente comando:

mogrify -format jpg *.png

A continuación se borran todos los pngs

2) Las imagenes son en grayscale, por tanto 1 byte para cada pixel. Las librerías de tensorflow se esperan 3 bytes para cada pixel.

Ejecutanos el script convertRGB.py

3) Una vez tenemos las imagenes en RGB, generamos las imagenes de salida

Ejecutanos el script generateTarget.py
