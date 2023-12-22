from flask import Flask, request
from celery import Celery

app = Flask(__name__)
celery = Celery(__name__)

# Настройки Celery
celery.conf.broker_url = 'pyamqp://guest:guest@localhost//'

@celery.task
def process_webhook(data):
    # Обработка веб-хука здесь, например, сохранение в базу данных
    print("Processing webhook:", data)

@app.route('/webhook', methods=['POST'])
def webhook_handler():
    data = request.json

    # Поместить веб-хук в очередь для асинхронной обработки
    process_webhook.delay(data)

    return "Webhook received and processing started."

if __name__ == '__main__':
    app.run(debug=True)

