# python-online-tetris
Es un juego de tetris basado en JavaScript, que mediante el Framework Django permite jugar online con otros jugadores en tiempo real.

https://online-tetris.herokuapp.com/

# Instrucciones de desarrollo
===============================


### 1) Para iniciar el desarrollo primero clonar el repositorio
```
# git clone [URL]
```

### 2) Instalar gitflow
Que es git-flow? (https://danielkummer.github.io/git-flow-cheatsheet/)

MAC:
```
# brew install git-flow
```
LINUX:
```
# apt-get install git-flow 
```

### 3) Iniciar gitflow
```
# git flow init
```

### 4) Crear feature para desarrollar en paralelo (branch)
```
# git flow feature start [NOMBRE FEATURE]
# git flow feature publish [NOMBRE FEATURE]
```

### 5) Para subir cambios en la feature
```
# git add .
# git commit -m "mejoras que se han hecho"
# git push origin feature/[NOMBRE FEATURE]
```

Debemos añadir el editor por defecto que queremos (nano o vim)
```
# git config --global core.editor "nano"
```

Cuando queramos finalizar la feature
```
git flow feature finish [NOMBRE FEATURE]
git flow release start [NOMBRE RELEASE]
git flow release finish [NOMBRE RELEASE]
git push --tags
```

### 6) 	Ahora vamos a preparar django para poder ejecutar el proyecto, para eso debemos crear el entorno virtual que debe situarse fuera de la carpeta donde esta git, es decir debemos estar en el directorio que contiene el repositorio clonado:
	
```
user$ ls
python-online-tetris

```

### 7) 	Una vez aqui ejecutamos la creacion del entorno virtual puede que sea necesario instalar virtualenv si no esta en el sistema
	
```
# virtualenv -p python3 env
```

Una vez terminado el proceso se creará un nuevo directorio llamado "env"

```
user$ ls
env                  python-online-tetris
```


### 8) 	Para desarrollar el proyecto sera necesario activar siempre en entorno virtual podremos hacerlo:
	
```
# source env/bin/activate

Cuando terminemos de desarrollar podemos desactivarlo

# source env/bin/deactivate
```

### 9)	Ahora ya tenemos el entorno virtual activado, vamos a instalar los requirements.txt para hacerlo entramos en el directorio que contiene el repositorio clonado de git "python-online-tetris".
	
```
# source env/bin/activate
# cd  python-online-tetris
# pip install -r requirements.txt 
```

### 10)	Una vez instalados los requirements ya podemos iniciar el server local

```
# python manage.py runserver
```

Deberia aparecer este log:

```
You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

December 15, 2017 - 17:09:30
Django version 1.10.8, using settings 'online_tetris.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Este log nos indica que antes de poder iniciar debemos hacer la base de datos local que se 
auto-genera en sqlite.

### 11)	Creamos la base de datos local
```
# python manage.py migrate
# python manage.py makemigrations online_tetris 
# python manage.py migrate online_tetris
```

### 12) Ya tenemos la base de datos local ahora ya podemos iniciar el server e ir con el navegador a la dirección http://127.0.0.1:8000/ para ver el estado de nuestro desarrollo
	
```
# python manage.py runserver
```
Para detener el server local CONTROL-C



### 13) Acceso al admin (gestor de los datos que hay en la BD), para tener acceso debemos crear un superusuario
```
# python manage.py createsuperuser
```
Una vez creado poniendo una contraseña y un nombre podremos ver el admin accediendo a http://localhost:8000/admin/

### 14) Instalar HEROKU (server)

```
MAC:
# brew install heroku/brew/heroku

Ubuntu:
# wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh
```

### 15) Acceso a la cuenta de HEROKU
```
heroku login
```

Accedemos al Dyno (repositorio del server)
```
heroku git:remote -a online-tetris
```

### 16) Para probar heroku en local (http://0.0.0.0:5000) :
```
heroku local web
```

### 17) Para hacer un deployment en el server (https://online-tetris.herokuapp.com/):
```
git push heroku master
```

===========================================================================

ANNEX:

DEPLOY CON DJANGO BUILDER:

#### [urls.py]
```
from django.contrib import admin 		
url(r'^admin/', include(admin.site.urls) ), 
```


#### [settings.py]

```
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATIC_URL = '/static/'
```


