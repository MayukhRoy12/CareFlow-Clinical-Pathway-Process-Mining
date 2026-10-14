import pandas as pd
import matplotlib.pyplot as plt
import os

def analyze_clinical_pathways(csv_path="data/cleaned_clinical_events.csv", report_dir="reports"):
    print("Loading cleaned event data...")
    df = pd.read_csv(csv_path)
    
    # Ensure the reports directory exists
    os.makedirs(report_dir, exist_ok=True)
    
    # 1. Activity Frequency Analysis
    print("Analyzing clinical activity frequencies...")
    activity_counts = df['concept:name'].value_counts()
    
    plt.figure(figsize=(10, 6))
    activity_counts.plot(kind='bar', color='steelblue')
    plt.title('Frequency of Clinical Activities in CareFlow')
    plt.xlabel('Clinical Activity')
    plt.ylabel('Total Count (Events)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    chart_path = os.path.join(report_dir, "activity_frequencies.png")
    plt.savefig(chart_path)
    print(f"Activity frequency chart saved to: {chart_path}")
    
    # 2. Process Discovery: Extract Most Common Pathways (Variants)
    print("Extracting most common patient pathways...")
    # Group by Case ID to capture the chronological sequence of events per patient
    pathways = df.groupby('case:concept:name')['concept:name'].apply(lambda x: ' -> '.join(x)).reset_index()
    pathways.columns = ['Case_ID', 'Pathway']
    
    # Count how many patients followed each exact pathway
    pathway_counts = pathways['Pathway'].value_counts().reset_index()
    pathway_counts.columns = ['Clinical_Pathway', 'Patient_Count']
    
    variants_path = os.path.join(report_dir, "common_pathways.csv")
    pathway_counts.to_csv(variants_path, index=False)
    print(f"Pathway variants report saved to: {variants_path}")

if __name__ == "__main__":
    analyze_clinical_pathways()