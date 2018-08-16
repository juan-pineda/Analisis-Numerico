
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

## Instalando Python en Linux:

### Tutorial
https://www.pugetsystems.com/labs/hpc/How-to-Install-Anaconda-Python-and-First-Steps-for-Linux-and-Windows-917/

En resumen...

1. Descargar [Anaconda:](https://www.anaconda.com/download/#linux)

2. Checar la integridad del archivo verificando la suma
“sha”. Tal suma identifica de forma única al archivo
descargado, y se encuentra pulsando [aquí](https://docs.continuum.io/anaconda/hashes/)
El sha de la página debe coincidir con el sha de nuestro archivo,
verifíquelo con el siguiente comando, cambiando al nombre de archivo
specífico que se haya descargado:  
`sha256sum Anaconda3-4.3.1-Linux-x86_64.sh`  

3. Correr el archivo de instalación desde un terminal (cambiar al nombre de archivo
específico que se haya descargado):  
`bash Anaconda3-4.3.1-Linux-x86_64.sh`

4. En caso de duda, seguir las configuraciones por defecto. Si le preguntan,
autorizar a conda a actualizar la variable PATH para que conda y python
sean visibles para todo el sistema. En otro caso, posiblemente tendremos
que hacerlo a mano.

## Usando Python:

Hay diferentes maneras de trabajar. Por ahora, para sesiones interactivas utilizaremos la interface interactiva conocida como **ipython**. Para abrirla, desde un terminal digite

```
ipython
```

Si en cambio deseamos crear un programa con toda una serie de instrucciones, y luego pedirle a python que las interprete de forma contínua, debemos almacenar el archivo con la extensión `.py`  y luego lo rodamos desde un terminal así:

```
python mi_primer_script.py
```




