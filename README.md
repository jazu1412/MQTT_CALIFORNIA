# California Water Resources MQTT System

This system monitors water mark levels (WML) across California's reservoirs using MQTT protocol for data collection and reporting.

## System Components

1. **Publisher (publisher.py)**
   - Reads water level data from CSV files
   - Converts data to JSON format
   - Publishes to specific MQTT topics for each reservoir (e.g., SHASTA/WML)

2. **Subscriber (subscriber.py)**
   - Subscribes to all reservoir topics
   - Collects and processes incoming data
   - Generates daily reports with water levels for each reservoir

## Data Format

The system uses the following data format:
- Input: CSV files with Date and TAF (Thousand Acre Feet) columns
- MQTT Messages: JSON format with timestamp and taf values
- Output: Daily reports showing water levels for each reservoir

## Usage

1. Start the MQTT broker (if not already running):
   ```bash
   mosquitto
   ```

2. Start the subscriber:
   ```bash
   python subscriber.py
   ```

3. Run the publisher:
   ```bash
   python publisher.py
   ```

## Reports

Daily reports are generated automatically and saved as text files in the format `report_MM_DD_YYYY.txt`. Each report includes:
- Individual reservoir water levels in TAF
- Total water capacity across all reservoirs

## Sample Data Sources
The system includes sample data for three reservoirs:
- Shasta Reservoir
- Oroville Reservoir
- Sonoma Reservoir

Each data source provides daily water mark levels in TAF (Thousand Acre Feet).
