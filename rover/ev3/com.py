import paho.mqtt.client as mqtt

class Com:
    def __init__(self,broker):
        self.callbacks = []
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.client.connect(broker,1883,60)

    def start(self):
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()

    def send_receive(self):
        self.client.loop()

    def on_connect(self,client, userdata, flags, rc):
        print("*** communication system online *** " + str(rc))
        self.client.publish("robot/status","ready")
        self.client.subscribe("robot/newplan")

    def on_publish(self,client, userdata, mid):
        pass

    def on_message(self, client, userdata, msg):
        for fn in self.callbacks:
            fn(userdata,msg)

    def subscribe(self, callback):
        self.callbacks.append(callback)

    def publish(self, topic, payload):
        self.client.publish(topic=topic,payload=payload)

    def heartbeat(self,payload):
        self.client.publish(topic="robot/heartbeat", payload=payload)
