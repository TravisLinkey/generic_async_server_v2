from flask import Flask
from flask_celery import make_celery
from utilities.utils import read_creds_file

# read the JSON creds file
data = read_creds_file('creds.json')

app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL=data["broker_url"],
    CELERY_RESULT_BACKEND=data["db_url"]
)


celery = make_celery(app)


# TODO - Sync Functions
@app.route('/process/<name>')
def process(name):
    reverse.delay(name)
    return 'Async Request Sent'


# TODO - Async Functions
@celery.task(name='main.reverse')
def reverse(string):
    return string[::-1]


if __name__ == '__main__':
    app.run(debug=True)
