# import librarya
import paho.mqtt.client as mqtt
import numpy


# inisialisasi broker
topik = "Photo"
broker_address = "127.0.0.1"

# inisialisasi client
print("menyiapkan instance")
pub = mqtt.Client("Publisher")

# Koneksi client dengan broker
pub.connect(broker_address, port=1883)
print("Terhubung ke broker")

# Baca File
file_dir = str(input("Direktori foto : "))

# buka file surf.jpg
file = open(file_dir, "rb")

# baca semua isi file
gambar = file.read()

# publish dengan topik photo dan data dipublish adalah file
print("Publish foto")
pub.publish(topik, gambar)

# client loop mulai
pub.loop_stop()

# tutup file
