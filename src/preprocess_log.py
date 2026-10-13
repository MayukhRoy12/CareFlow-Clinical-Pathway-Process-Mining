import pandas as pd
import pm4py
import os

def preprocess_event_log(input_path="data/raw_clinical_events.csv", output_dir="data"):
    print(f"Loading raw data from {input_path}...")
    df = pd.read_csv(input_path)

    # 1. Convert timestamp to datetime objects
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # 2. Sort by Case ID and Timestamp (Critical for process sequence)
    df = df.sort_values(by=['case_id', 'timestamp'])

    # 3. Rename columns to PM4Py standard terminology
    df.rename(columns={
        'case_id': 'case:concept:name',
        'activity': 'concept:name',
        'timestamp': 'time:timestamp'
    }, inplace=True)

    # 4. Save the cleaned standard CSV
    cleaned_csv_path = os.path.join(output_dir, "cleaned_clinical_events.csv")
    df.to_csv(cleaned_csv_path, index=False)
    print(f"Cleaned CSV saved to: {cleaned_csv_path}")

    # 5. Format for PM4Py and export as standard XES log
    print("Formatting and exporting PM4Py Event Log...")
    event_log = pm4py.format_dataframe(
        df, 
        case_id='case:concept:name', 
        activity_key='concept:name', 
        timestamp_key='time:timestamp'
    )
    
    xes_path = os.path.join(output_dir, "clinical_event_log.xes")
    pm4py.write_xes(event_log, xes_path)
    print(f"XES Event Log saved successfully to: {xes_path}")

if __name__ == "__main__":
    preprocess_event_log()