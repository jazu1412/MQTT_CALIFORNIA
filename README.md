# California Reservoir Water Level Monitoring System

A real-time water level monitoring system for California reservoirs using MQTT protocol. This system processes and publishes water level data from multiple reservoirs and generates daily reports.

## Overview

This project implements a publisher-subscriber architecture using MQTT to monitor water levels (in TAF - Thousand Acre Feet) across three major California reservoirs:
- Shasta
- Oroville
- Sonoma

## System Requirements

- Python 3.x
- paho-mqtt library
- Running MQTT broker (e.g., Mosquitto) on localhost:1883

## Installation

1. Install the required Python package:
```bash
pip install paho-mqtt
```

2. Ensure you have an MQTT broker running on localhost:1883

## File Structure

- `publisher.py` - Reads CSV data and publishes to MQTT topics
- `subscriber.py` - Subscribes to MQTT topics and generates reports
- `*_WML(Sample).csv` - Sample water level data files for each reservoir
- `report_*.txt` - Generated daily reports

## Usage

1. Start the subscriber:
```bash
python subscriber.py
```

2. In a separate terminal, run the publisher:
```bash
python publisher.py
```

## Data Format

### Input CSV Format
Each reservoir's CSV file should contain:
- Date: Date of measurement
- TAF: Water level in Thousand Acre Feet

### MQTT Topics
The system uses the following topics:
- SHASTA/WML
- OROVILLE/WML
- SONOMA/WML

### Message Format
Messages are published in JSON format:
```json
{
    "timestamp": "date",
    "taf": float_value
}
```

## Daily Reports

The subscriber generates daily reports (`report_*.txt`) containing:
- Individual reservoir water levels
- Total water capacity across all reservoirs
- Timestamp of measurements

## Error Handling

The system includes error handling for:
- MQTT connection failures
- File reading/writing operations
- Data parsing issues

## Notes

- Data is published with a 1-second delay between messages
- Reports are automatically generated and updated as new data arrives
- The system can be extended to include additional reservoirs by modifying the topics list and adding corresponding CSV files
