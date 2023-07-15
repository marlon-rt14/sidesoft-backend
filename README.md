#SIDESOFT - BACKEND
## 1. Correr el proyecto localmente

* **Virtual Enviornment** - Recomendamos trabajar en un entorno virtual siempre que se utilice Python para proyectos. Esto mantiene tus dependencias para cada proyecto separadas y organizadas. Las instrucciones para configurar un entorno virtual para su plataforma se pueden encontrar en la sección [documentación de python](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
<br>

* **Activa el entorno virtual**

Antes que nada, activa el entorno virtual corriendo estos comandos:

```bash
# En Windows:
venv\Scripts\activate
# En Linux:
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
```
<br>

* **PIP Dependencias** - Una vez que tengas tu entorno virtual configurado y funcionando, instala las dependencias navegando hasta el directorio del proyecto y ejecutando:
```bash
# En Windows:
py -m pip install -r requirements.txt
# En Linux:
pip install -r requirements.txt
```
Esto instalará todos los paquetes necesarios que seleccionamos en el archivo `requirements.txt`.
<br>


* **Variables de entorno**
Renombra el archivo `.env.develop` a `.env` y configura los valores de las varialbes de entorno 
<br>

* **Inicia el servidor**
Abre el en tu navegador [http://localhost:5000/](http://localhost:5000/)
```bash
# On Windows:
py ./server/index.py
# On Linux:
python3 ./server/index.py
```
## 2. Usando Docker
* Ubicate en el directoria del proyecto
* Configura las variables de entorno del proyecto en la siguiente seccion:

```
ENV DEBUG=False
ENV SERVER_PORT=5000
ENV SECRET_KEY=whoismarlon
```
<br/>

* Ejecuta el siguiente comando para crear la imagen:
```bash
docker build . -t sidesoft-backend
```

* Crea un contenedor
```bash
docker run --name mysidesoft-back -p 5000:5000 sidesoft-backend
```
