# MQTT → ThingSpeak Forwarder
Mengambil data dari MQTT broker lalu mengirimkannya ke ThingSpeak setiap 15 detik.

## Environment Variables
- MQTT_BROKER
- MQTT_PORT
- MQTT_TOPIC
- THINGSPEAK_API_KEY

## Cara Run Lokal
pip install -r requirements.txt
python3 main.py
