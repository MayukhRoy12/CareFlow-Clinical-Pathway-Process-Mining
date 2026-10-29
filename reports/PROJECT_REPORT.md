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
* **Standardization:** Conversion of raw timestamps and activities into the standard XES (eXtensible Event Stream) format to ensure compatibility with advanced process mining frameworks.

## 4. Process Discovery & EDA
The exploratory data analysis revealed distinct operational patterns within the clinical pathways. The most frequent variant followed a standard progression: ER Triage -> Initial Clinical Assessment -> Blood Test & Lab Work -> Medication Administration -> Discharge Assessment -> Post-Care Discharge. Deviations from this standard pathway primarily occurred in cases with "High" or "Critical" severity, where patients were diverted to Diagnostic Imaging, Specialist Consultations, and Surgical Interventions, significantly increasing the complexity of the process model.

## 5. Performance & Bottleneck Analysis
Performance analysis highlighted critical areas for operational improvement. Throughput time variance was heavily dependent on patient severity. The bottleneck analysis exposed the most severe delays in the system:
1.  **Diagnostic Imaging to Specialist Review:** Patients experienced prolonged wait times after X-Ray/CT scans before a specialist was available for consultation.
2.  **Surgical Intervention to Inpatient Bed Admission:** The highest average transition delay occurred when transferring critical patients from surgery to the ICU, indicating a severe shortage of available inpatient beds or a lag in ward turnaround times.

## 6. Conclusion & Recommendations
The CareFlow process mining analysis successfully transformed raw event data into clear operational insights. To optimize patient flow, healthcare administrators should:
*   **Reallocate Resources:** Increase staffing during peak diagnostic imaging hours to reduce the backlog awaiting specialist review.
*   **Optimize Bed Management:** Implement predictive alerting for ICU bed requirements as soon as a patient is scheduled for surgical intervention to eliminate the postoperative bottleneck.
*   **Continuous Monitoring:** Utilize the CareFlow interactive dashboard to monitor transition times in real-time, ensuring proactive intervention before minor delays cascade into critical throughput failures.