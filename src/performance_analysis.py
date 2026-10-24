import pandas as pd
import matplotlib.pyplot as plt
import os

def analyze_performance(csv_path="data/cleaned_clinical_events.csv", report_dir="reports"):
    """
    Calculates patient throughput times and identifies clinical bottlenecks.
    
    This function analyzes the time elapsed between consecutive clinical events
    to measure the overall throughput duration for each patient. It also calculates
    the average waiting times between specific pathway transitions, exposing the 
    most severe bottlenecks in the healthcare system. It outputs a comprehensive
    throughput CSV and a horizontal bar chart of the top 10 bottlenecks.
    
    Args:
        csv_path (str): File path to the cleaned standard event log CSV.
        report_dir (str): Directory where the generated performance reports are saved.
    """
    print("Loading event data for performance analysis...")
    df = pd.read_csv(csv_path)
    
    # Ensure datetime format
    df['time:timestamp'] = pd.to_datetime(df['time:timestamp'])
    
    # 1. Calculate Throughput Time (Total duration per patient)
    print("Calculating patient throughput times...")
    throughput = df.groupby('case:concept:name')['time:timestamp'].agg(['min', 'max'])
    throughput['duration_hours'] = (throughput['max'] - throughput['min']).dt.total_seconds() / 3600
    
    throughput_path = os.path.join(report_dir, "patient_throughput.csv")
    throughput.to_csv(throughput_path)
    print(f"Throughput data saved to: {throughput_path}")
    
    # 2. Identify Bottlenecks (Time between consecutive events)
    print("Identifying process bottlenecks...")
    # Shift columns to align current activity with the next activity for the same patient
    df['next_activity'] = df.groupby('case:concept:name')['concept:name'].shift(-1)
    df['next_timestamp'] = df.groupby('case:concept:name')['time:timestamp'].shift(-1)
    
    # Calculate transition time in hours
    df['transition_time_hours'] = (df['next_timestamp'] - df['time:timestamp']).dt.total_seconds() / 3600
    
    # Filter out the final events (which have no subsequent activity)
    transitions = df.dropna(subset=['next_activity', 'transition_time_hours']).copy()
    transitions['transition_name'] = transitions['concept:name'] + " -> " + transitions['next_activity']
    
    # Calculate the average wait time for each transition pathway
    avg_wait_times = transitions.groupby('transition_name')['transition_time_hours'].mean().sort_values(ascending=False).head(10)
    
    # 3. Visualize Top 10 Bottlenecks
    plt.figure(figsize=(12, 6))
    avg_wait_times.plot(kind='barh', color='salmon')
    plt.title('Top 10 Clinical Bottlenecks (Average Wait Time in Hours)')
    plt.xlabel('Average Wait Time (Hours)')
    plt.ylabel('Clinical Transition Pathway')
    plt.gca().invert_yaxis()  # Place highest wait time at the top
    plt.tight_layout()
    
    bottleneck_chart_path = os.path.join(report_dir, "bottlenecks.png")
    plt.savefig(bottleneck_chart_path)
    print(f"Bottleneck chart saved to: {bottleneck_chart_path}")

if __name__ == "__main__":
    analyze_performance()