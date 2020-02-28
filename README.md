# Satelite de Noticias de BCCH
**Una plataforma de noticias del eje tecnologico del observatorio tecnologico de BCCH en Django, Django REST Framework y Vue JS**

Referencia para la creacion de esta plataforma:
English Version:(https://www.udemy.com/course/the-complete-guide-to-django-rest-framework-and-vue-js/?referralCode=A2FA0F6C1C4BE66A3B3E)

Hasta el momento (Febrero 27, 2020) es de forma local 

## Hot to set up the project to run on your local machine?

#### Download the code to your PC, unpack the zip and move inside the folder.

#### Create a new Python Virtual Environment:
```
python3 -m venv venv
```

#### Activate the environment and install all the Python/Django dependencies:

SI SE ESTA EN MAC:
Vaya al requirements.txt y borre la linea de pkg-resource entera y guarde el cambio


SINO HAGA SOLAMENTE:
```
source venv/bin/activate
pip install -r requirements.txt
```

#### Apply the migrations as usual in the folder with the manage.py file.
```
python manage.py makemigrations
python manage.py migrate
```

#### Time to install the Vue JS dependencies:
```
cd SateliteNoticias/frontend
npm install
```

#### Run Vue JS Development Server:
```
npm run serve

#### Run Django's development server:
```
python manage.py runserver
```

#### Open up Chrome and go to 127.0.0.1:8000 and the app is now running in development mode! (Febrero 27, 2020)

