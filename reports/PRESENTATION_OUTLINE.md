# CareFlow: Clinical Pathway Process Mining - Final Presentation

## Slide 1: Title Slide
* **Project:** CareFlow: Clinical Pathway Process Mining
* **Author:** Mayukh Roy
* **Role:** Data Associate L1 Intern, Data Analytics
* **Company:** Infotact Solutions
* **Mentors/Guides:** Dr. Soumyendu Banerjee & Dr. Arnab Ghosh

## Slide 2: Problem Statement
* Healthcare facilities struggle with hidden inefficiencies and patient bottlenecks.
* Traditional analytics often fail to capture the true chronological sequence of patient care.
* **Objective:** Apply Process Mining to clinical event logs to visualize actual patient journeys and identify delays.

## Slide 3: Methodology & Tech Stack
* **Data Engineering:** Python, Pandas (Generated 500+ patient event logs)
* **Process Mining:** PM4Py (Converted raw data into XES standard formats)
* **Visualization:** Matplotlib, Streamlit (Interactive dashboard for real-time tracking)

## Slide 4: Key Insights & Bottlenecks
* **Insight 1:** Most standard pathways follow Triage -> Lab Work -> Discharge.
* **Insight 2 (Bottleneck):** Significant delays occur between Diagnostic Imaging and Specialist Consultations.
* **Insight 3 (Bottleneck):** Critical patients face severe wait times transitioning from Surgical Intervention to Inpatient Bed Admissions.

## Slide 5: Business Impact & Conclusion
* **Resource Optimization:** Reallocating staff during peak imaging hours reduces wait times.
* **Actionable Monitoring:** The Streamlit dashboard enables administrators to track throughput in real-time, preventing cascading delays.