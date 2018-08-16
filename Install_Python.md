
## Install Python on windows via Anaconda (recomendado):

### Tutorial:
https://medium.com/@GalarnykMichael/install-python-on-windows-anaconda-c63c7c3d1444

### Descargar Anaconda:
https://www.anaconda.com/download/#windows

Instalar Anaconda usando el archivo ejecutable.
En caso de duda durante la instalación, simplemente mantener las configuraciones por defecto.
**Importante:** Activar la casilla _“Add Anaconda to my PATH environment variable”_

Para testar:
1. Abrir un terminal “Anaconda prompt”.
2. Digitar los siguientes comandos y ver si los reconoce

   ```
   conda list
   python --version
   jupyter notebook  # Debe abrir un jupyter notebook en el navegador de internet
   where python
   where conda
   ```
   
[//]: # (Si no activaron la casilla para actualizar el PATH, hay que hacerlo manualmente.
Abrir el “command prompt” o el “cmd”, y digitar algo como:
`SETX PATH “%PATH%;C:\...\....;C:\...\...\Anaconda2`
Donde los dos paths sugeridos deben corresponder a las salidas en el “anaconda prompt” de los comandos:   
```
where python 
where conda
```)

Para que el sistema detecte los cambios en PATH hay que cerrar el terminal y abrir uno nuevo, para que el sistema lea de nuevo el archivo de configuraciones.

Python ya debería estar disponible. Para asegurarse, en el “cmd” digitar:
`python`

## Instalando Python en Linux:

### Tutorial
https://www.pugetsystems.com/labs/hpc/How-to-Install-Anaconda-Python-and-First-Steps-for-Linux-and-Windows-917/

En resumen...

1. Descargar [Anaconda:](https://www.anaconda.com/download/#linux)

2. Checar la integridad del archivo (sin errores) corroborando si la suma de
verificación “sha” corresponde con lo que debería ser. Es única del archivo
descargado y se encuentra [aquí](https://docs.continuum.io/anaconda/hashes/)
El sha de nuestro archivo se verifica así (deben coincidir):   
`sha256sum Anaconda3-4.3.1-Linux-x86_64.sh`  

3. Correr el archivo de instalación desde un terminal (cambiar al nombre de archivo
específico que se haya descargado):  
`bash Anaconda3-4.3.1-Linux-x86_64.sh`

4. En caso de duda, seguir las configuraciones por defecto. Si le preguntan,
autorizar a conda a actualizar la variable PATH para que conda y python
sean visibles para todo el sistema. En otro caso, posiblemente tendremos
que hacerlo a mano.

2. Checar la integridad del archivo (sin errores) corroborando si la suma de
verificación “sha” corresponde con lo que debería ser. Es única del archivo
descargado y se encuentra [aquí](https://docs.continuum.io/anaconda/hashes/)
El sha de nuestro archivo se verifica así (deben coincidir):   
`sha256sum Anaconda3-4.3.1-Linux-x86_64.sh`  

3. Correr el archivo de instalación desde un terminal:  
`bash Anaconda3-4.3.1-Linux-x86_64.sh`

4. En caso de duda, seguir las configuraciones por defecto. Si le preguntan,
autorizar a conda a actualizar la variable PATH para que conda y python
sean visibles para todo el sistema. En otro caso, posiblemente tendremos
que hacerlo a mano.

## Usando Python:

Hay diferentes maneras de trabajar:

```python
python mi_primer_script.py
ipython
jupyter notebook
```

## Primeros pasos:

Trabajar los siguientes notebooks:

* 00_Quick_Python_Intro.ipynb
* numerical-slides.ipynb








