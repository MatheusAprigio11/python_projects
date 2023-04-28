from paho.mqtt import client as mqtt
from paho.mqtt import publish
clientBro = "pedrinho"
port = 1833
broker = "10.21.160.16"

client = mqtt.Client()
client.connect(broker, port)

publish.single(clientBro, "pedrinho maravilhoso", hostname=broker, port=port)
