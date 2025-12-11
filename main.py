import paho.mqtt.client as mqtt
import json
import requests
import time
import sys
import os

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# --- Konfigurasi via Environment Variable ---
BROKER = os.getenv("MQTT_BROKER", "103.217.145.168")
PORT = int(os.getenv("MQTT_PORT", 1883))
TOPIC = os.getenv("MQTT_TOPIC", "data/sctkiotserver/groupsctkiotserver/123")

THINGSPEAK_API_KEY = os.getenv("THINGSPEAK_API_KEY", "")
THINGSPEAK_URL = "https://api.thingspeak.com/update"

FIELDS_MAP = {
    "PRESSURE_DST": "field1",
    "LVL_RES_WTP3": "field2",
    "TOTAL_FLOW_ITK": "field3",
    "TOTAL_FLOW_DST": "field4",
    "FLOW_WTP3": "field5",
    "FLOW_CARENANG": "field6",
    "FLOW_CIJERUK": "field7",
    "FLOW_50_WTP1": "field8",
}

def send_to_thingspeak(data):
    payload = {"api_key": THINGSPEAK_API_KEY}

    for key, field in FIELDS_MAP.items():
        if key in data:
            try:
                payload[field] = float(data[key])
            except:
