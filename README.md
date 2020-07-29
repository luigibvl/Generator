# Generator

Per avviare l'applicazione occorre aver installato una distribuzione di R.

Effettuata l'installazione vanno digitati i comandi

* python3 manage.py makemigrations
* python3 manage.py migrate 
* python3 manage.py collectstatic
* python3 manage.py runserver

Inoltre, va avviato il brocker col comando

* rabbitmq-server  

ed infine Celery col comando (nel contesto del progetto)

* celery -A root worker -l info
