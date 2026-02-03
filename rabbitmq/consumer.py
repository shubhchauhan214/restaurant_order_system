import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue',durable=True)

def callback(ch, method, properties, body):
    print(" [x] Received:", body.decode())


    try:
        data = json.loads(body)
        print("Processed data:", data)
    
    except Exception:
        pass

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='task_queue',on_message_callback=callback)

channel.start_consuming()