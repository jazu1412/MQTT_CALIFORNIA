import paho.mqtt.client as mqtt
import csv
import json
import time
from datetime import datetime

# MQTT Broker settings
BROKER = "localhost"
PORT = 1883

# Initialize MQTT client
client = mqtt.Client()

def connect_mqtt():
    try:
        client.connect(BROKER, PORT)
        print(f"Connected to MQTT Broker: {BROKER}")
        return True
    except Exception as e:
        print(f"Failed to connect to broker: {e}")
        return False

def read_csv_and_publish(file_name, topic):
    try:
        with open(file_name, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convert data to JSON format
                data = {
                    "timestamp": row['Date'],
                    "taf": float(row['TAF'])
                }
                # Publish to MQTT topic
                message = json.dumps(data)
                client.publish(f"{topic}/WML", message)
                print(f"Published to {topic}/WML: {message}")
                time.sleep(1)  # Add delay between publications
    except Exception as e:
        print(f"Error processing {file_name}: {e}")

def main():
    if connect_mqtt():
        # Define reservoir data sources
        reservoirs = [
            ("Shasta_WML(Sample),.csv", "SHASTA"),
            ("Oroville_WML(Sample),.csv", "OROVILLE"),
            ("Sonoma_WML(Sample),.csv", "SONOMA")
        ]

        # Process each reservoir's data
        for csv_file, topic in reservoirs:
            print(f"\nProcessing {csv_file}...")
            read_csv_and_publish(csv_file, topic)

        client.disconnect()
        print("\nDisconnected from MQTT broker")

if __name__ == "__main__":
    main()
