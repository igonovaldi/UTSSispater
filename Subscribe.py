# gunakan library paho
import paho.mqtt.client as mqtt
import numpy

# gunakan library time
import time

# buat callback pada saat ada pesan masuk
###########################################


def on_message(client, userdata, message):
    # tulis hasil file yang didapat bernama "iris.jpg"
    file_name = str(input("Nama file : "))
    file = open("iris.jpg", "wb")
    file.write(message.payload)
    file.close()
    ##########################################


    # definisikan broker yang akan digunakan
topik = "Photo"
broker_address = "127.0.0.1"

# buat client P2
print("menyiapkan instance")
sub = mqtt.Client("Sub")

# koneksi P2 ke broker
print("terhubung ke broker")
sub.connect(broker_address, port=1883)

# P2 subcribe ke topik "photo"
print("Subscribing ke topik:", "photo")
sub.subscribe(topik)

# callback diaktifkan
sub.on_message = on_message

# client.loop_forever()
while True:
    sub.loop(15)
    time.sleep(2)