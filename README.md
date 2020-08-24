## Tech Stack:

Celery and Flask Servers, SQLite3 backend, RabbitMQ Server on Heroku

### Step 1 - Run Celery Server

celery -A main.celery worker --loglevel=info

### Step 2 - Run Flask App Server

python main.py
