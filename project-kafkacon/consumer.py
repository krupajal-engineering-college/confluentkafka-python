import os
from confluent_kafka import Consumer

config = {
    'bootstrap.servers': 'pkc-9q8rv.ap-south-2.aws.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': os.getenv("KAFKA_API_KEY"),
    'sasl.password': os.getenv("KAFKA_API_SECRET"),
    'client.id': 'transaction-consumer',
    'group.id': 'transaction-consumer-group',
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': False,
}

consumer = Consumer(config)

topic = 'my_first_topic'
consumer.subscribe([topic])
try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue
        print(f"Received message: Key = {msg.key().decode('utf-8')} Value = {msg.value().decode('utf-8')}")
        consumer.commit(msg)
except KeyboardInterrupt:
    pass    

finally:
    consumer.close()          