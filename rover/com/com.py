"""Com subsystem."""
import paho.mqtt.client as mqtt


class Com:
    """implements communication subsystem."""

    def __init__(self, broker):
        """Create a communication subsystem.

        arguments:
            broker -- address for MQTT broker

        """
        self.callbacks = []
        self.broker = broker
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(broker, 1883, 60)
        self.client.loop_start()

    def publish(self, topic, payload):
        """Publish a message to communication system.

        arguments:
            topic -- topic for message ex robot/status
            payload -- data to send along with message

        """
        self.client.publish(topic=topic, payload=payload)


    def on_connect(self, client, userdata, flags, rc):
        """Run on_connect event."""
        print("*** COM System Initialized ***")
        self.client.subscribe("robot/status")

    def on_message(self, client, userdata, msg):
        payload = msg.payload.decode()
        for callback in self.callbacks:
            if callback[0] == msg.topic:
                callback[1](payload)

    def subscribe(self, topic, callback):
        self.callbacks.append((topic, callback))
