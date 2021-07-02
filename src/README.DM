# crear y activar un entorno virtual
python3 -m venv .venv
source .venv/bin/activate


# instalar requerimientos del proyecto
python3 -m pip install -r requirements.txt


# crear .PO para generar traducciones
django-admin makemessages -l en
django-admin makemessages -l es
django-admin makemessages -l es_MX


# generar binario de las traducciones
django-admin compilemessages


# aplicar migraciones para db.sqlite
python3 project/manage.py migrate


# Lanzar servidor de desarrollo
python3 manage.py runserver
