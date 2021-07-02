# Crear y activar un entorno virtual
python3 -m venv .venv

source .venv/bin/activate


# Instalar requerimientos del proyecto
python3 -m pip install -r requirements.txt


# Crear .PO para generar traducciones
django-admin makemessages -l en

django-admin makemessages -l es

django-admin makemessages -l es_MX


# Generar binario de las traducciones
django-admin compilemessages


# Aplicar migraciones para db.sqlite
python3 project/manage.py migrate


# Lanzar servidor de desarrollo
python3 project/manage.py runserver
