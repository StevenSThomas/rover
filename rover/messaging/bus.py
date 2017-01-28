import paho.mqtt.client as mqtt


class Bus:

    def __init__(self,broker):
        self.broker = broker
        self.client = mqtt.Client()
        self.client.connect(broker,1883,60)

    def publish(self,topic,payload):
        self.client.publish(topic=topic, payload=payload)
