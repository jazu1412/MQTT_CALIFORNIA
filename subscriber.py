import paho.mqtt.client as mqtt
import json
from datetime import datetime
from collections import defaultdict

# MQTT Broker settings
BROKER = "localhost"
PORT = 1883

# Data storage for daily reports
daily_data = defaultdict(lambda: defaultdict(list))

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        # Subscribe to all reservoir topics
        topics = ["SHASTA/WML", "OROVILLE/WML", "SONOMA/WML"]
        for topic in topics:
            client.subscribe(topic)
            print(f"Subscribed to {topic}")
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    try:
        # Decode and parse the message
        payload = json.loads(msg.payload.decode())
        reservoir = msg.topic.split('/')[0]
        date = payload['timestamp']
        taf = payload['taf']

        # Store the data
        daily_data[date][reservoir].append(taf)
        
        # Generate report after receiving data
        generate_daily_report(date)
    except Exception as e:
        print(f"Error processing message: {e}")

def generate_daily_report(date):
    if date in daily_data:
        report = f"\nDaily Water Level Report - {date}\n"
        report += "=" * 50 + "\n"
        
        total_taf = 0
        for reservoir in sorted(daily_data[date].keys()):
            values = daily_data[date][reservoir]
            avg_taf = sum(values) / len(values)
            total_taf += avg_taf
            report += f"{reservoir:10} : {avg_taf:.2f} TAF\n"
        
        report += "=" * 50 + "\n"
        report += f"Total Capacity: {total_taf:.2f} TAF\n"
        
        # Save report to file
        with open(f"report_{date.replace('/', '_')}.txt", "w") as f:
            f.write(report)
        print(report)

def main():
    # Initialize MQTT client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(BROKER, PORT)
        print(f"Connecting to MQTT Broker: {BROKER}")
        client.loop_forever()
    except KeyboardInterrupt:
        print("\nDisconnecting from MQTT broker")
        client.disconnect()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
