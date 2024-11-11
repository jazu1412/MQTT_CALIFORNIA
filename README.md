# MQTT Data from California Reservoirs and Report

## Overview
The California Department of Water Resources aims to evaluate water availability across all state reservoirs. This is achieved by collecting Water Mark Levels (WML) from each reservoir and aggregating the data into a central repository for comprehensive reporting.

## Data Schema
The data is organized using a `Reservoir_ID/WML` schema. For example:
- Shasta reservoir reports to the `SHASTA/WML` topic.
- Oroville reservoir reports to the `OROVILLE/WML` topic.
- Sonoma reservoir reports to the `SONOMA/WML` topic.

## Process
1. **MQTT Publishers:** Sensors at each reservoir act as publishers, posting data to specific topics.
2. **MQTT Subscribers:** A single subscriber collects data from these topics to produce daily summaries.
3. **Data Model:** JSON is used as the data model for this purpose.

## Sample Data
Sample data for three reservoirs is provided in CSV format:
- `Shasta_WML(Sample).csv`
- `Oroville_WML(Sample).csv`
- `Sonoma_WML(Sample).csv`

## Instructions
1. Convert the sample data from CSV to JSON.
2. Use MQTT publishers to send data to the respective reservoir topics.
3. Implement an MQTT subscriber to generate daily reports based on the collected data.

## TAF
Water reservoir capacities in the US are commonly given in thousands of acre-feet (TAF). In most other countries, the metric system is used.

## Files
- Shasta_WML(Sample).csv
- Oroville_WML(Sample).csv
- Sonoma_WML(Sample).csv
