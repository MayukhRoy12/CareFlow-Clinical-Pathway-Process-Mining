# CareFlow: Clinical Pathway Process Mining

## Project Objective
The objective of this project is to provide practical exposure to real-world Data Analytics workflows by analyzing healthcare event logs. This project aims to discover, map, and optimize patient treatment journeys to identify bottlenecks and generate actionable business insights.

## Project Structure
```text
CareFlow-Project/
│
├── data/                      # Contains raw and processed event logs
│   ├── raw_clinical_events.csv
│   ├── cleaned_clinical_events.csv
│   └── clinical_event_log.xes
├── notebooks/                 # Exploratory data analysis notebooks
├── reports/                   # Generated analytics, plots, and pathway metrics
│   ├── activity_frequencies.png
│   ├── bottlenecks.png
│   ├── common_pathways.csv
│   └── patient_throughput.csv
├── src/                       # Source code for the data pipeline
│   ├── generate_dataset.py    # Synthetic healthcare event log generator
│   ├── preprocess_log.py      # Event log standardization (PM4Py format)
│   ├── process_discovery.py   # Pathway extraction and frequency analysis
│   ├── performance_analysis.py # Throughput and bottleneck calculations
│   └── dashboard.py           # Streamlit interactive dashboard
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation

## Execution Guide
To run the complete CareFlow process mining pipeline locally, execute the following commands in order from the project root directory:

1. **Generate Synthetic Data:** `python src/generate_dataset.py`
2. **Preprocess and Standardize:** `python src/preprocess_log.py`
3. **Run Process Discovery:** `python src/process_discovery.py`
4. **Analyze Bottlenecks:** `python src/performance_analysis.py`
5. **Launch the Dashboard:** `streamlit run src/dashboard.py`