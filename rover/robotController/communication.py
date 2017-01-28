import paho.mqtt.client as mqtt

class Com:
    def __init__(self,broker):
        self.callbacks = []
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(broker,1883,60)


    def start(self):
        self.client.loop_forever()


    def on_connect(self,client, userdata, flags, rc):
        print("connected with result code " + str(rc))

        self.client.subscribe("robot/newplan")

    def on_message(self, client, userdata, msg):
        for fn in self.callbacks:
            fn(userdata,msg)

    def subscribe(self, callback):
        self.callbacks.append(callback)
