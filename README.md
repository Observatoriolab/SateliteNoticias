# Satelite de Noticias 
**Una plataforma de noticias del eje tecnologico en Django, Django REST Framework y Vue JS**

Referencia para la creacion de esta plataforma:
English Version:(https://www.udemy.com/course/the-complete-guide-to-django-rest-framework-and-vue-js/?referralCode=A2FA0F6C1C4BE66A3B3E)

Hasta el momento (Marzo 3, 2020) es de forma local 



## WINDOWS 10, MAC y Linux

## Dependencias (programas a instalar)

NODEJS, 
PYTHON 3.8.2, 
PIP (viene con python incluido), 
GIT 

Guia de instalacion (proximamente)

## CRONOLOGICAMENTE HACER:




#### *) Abrir el GIT BASH de Windows (al tener ya instalado GIT dada la guia de instalacion)
```
Click derecho y opcion GIT BASH
```

#### 0) Clonar el proyecto

git clone https://github.com/Observatoriolab/SateliteNoticias.git


#### 0.5) SI SE ESTA EN WINDOWS 10 HAY QUE MODIFICAR LA SIGUIENTE LINEA EN EL ARCHIVO vue.config.js :
```
publicPath: "http://0.0.0.0:8080/",
```
por 
```
publicPath: "http://127.0.0.1:8080/",
```
(como dice el comentario de // on Windows you might want to set publicPath: "http://127.0.0.1:8080/" )
Si no se esta en WINDOWS 10, se DEBE DEJAR TAL COMO ESTABA

#### 1) Crear el ambiente de desarrollo en la carpeta ya clonada

```
python -m venv venv
```

#### 2) Activar el ambiente de desarrollo e instalar todas las dependencias de Python/Django:
En WINDOWS 10
```
source venv/Scripts/activate
```
EN MAC/LINUX:
```
source venv/bin/activate
```
Despues de esto se instalan las dependencias con lo siguiente:

```
pip install -r requirements.txt
```

#### 3) Aplicar las migraciones de Django
```
cd SateliteNoticias
python manage.py makemigrations users
python manage.py makemigrations news

python manage.py migrate
```

#### 4) Correr el servidor de Django:
```
python manage.py runserver
```

#### 5) Instalacion de las dependencias de Vue JS :

En otra consola GIT BASH (si se esta en WIN10, sino terminal/consola) hacer:
```
cd SateliteNoticias/frontend
npm install
```

#### 6) Correr el servidor de desarrollo de Vue JS:
En esa misma carpeta hacer:
```
npm run serve
```


#### 7) Abrir chrome e ir a 127.0.0.1:8000 y alli esta el servidor de desarrollo andando (Marzo 3, 2020)

