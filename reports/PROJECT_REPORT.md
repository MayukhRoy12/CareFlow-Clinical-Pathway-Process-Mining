# CareFlow: Clinical Pathway Process Mining - Final Project Report

## 1. Executive Summary
The CareFlow project applies advanced Process Mining techniques to healthcare event logs to discover, map, and optimize patient treatment journeys. By analyzing a synthetic dataset representing 500 patient cases in an Emergency Department setting, this project successfully identified key clinical pathways and exposed critical operational bottlenecks. The resulting interactive dashboard provides actionable business insights, enabling healthcare administrators to visualize patient throughput, track care deviations, and target specific delays (such as imaging and inpatient bed admission wait times) for workflow optimization.

## 2. Methodology
This project utilizes a robust Data Analytics workflow centered around Process Mining. The methodology involves:
* **Data Engineering:** Utilizing Python and `pandas` to generate, clean, and chronologically sequence clinical event logs.
* **Standardization:** Leveraging the `pm4py` library to format the raw data into the industry-standard XES (eXtensible Event Stream) format.
* **Process Discovery:** Applying frequency analysis to extract the most common variants of patient care and identify deviations from standard clinical protocols.
* **Performance Analysis:** Calculating throughput times and transition delays to pinpoint inefficiencies.
* **Visualization:** Developing an interactive web-based dashboard using `streamlit` to democratize access to the generated analytics.

## 3. Data Pipeline & Preprocessing
* **Data Generation:** Synthetic dataset representing 500 patient journeys through an Emergency Department.
* **Standardization:** Conversion of raw timestamps and activities into the standard XES (eXtensible Event Stream) format.

## 4. Process Discovery & EDA
*(To be completed: Summary of the most frequent clinical pathways, variant analysis, and activity volume.)*

## 5. Performance & Bottleneck Analysis
*(To be completed: Detailed breakdown of patient throughput times and the longest waiting periods between consecutive clinical activities.)*

## 6. Conclusion & Recommendations
*(To be completed: Final thoughts on how these insights could be used to optimize healthcare delivery and reduce patient wait times.)*