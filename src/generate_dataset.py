import os
import random
from datetime import datetime, timedelta
import pandas as pd


def generate_clinical_event_log(num_patients=500, random_seed=42):
    random.seed(random_seed)

    activities_pool = [
        "ER Triage",
        "Initial Clinical Assessment",
        "Blood Test & Lab Work",
        "Diagnostic Imaging (X-Ray/CT)",
        "Specialist Consultation",
        "Medication Administration",
        "Surgical Intervention",
        "Inpatient Bed Admission",
        "Discharge Assessment",
        "Post-Care Discharge",
    ]

    records = []
    base_time = datetime(2026, 9, 1, 8, 0, 0)

    for i in range(1, num_patients + 1):
        patient_id = f"PAT-{i:04d}"
        age = random.randint(18, 85)
        severity = random.choice(["Low", "Moderate", "High", "Critical"])

        # Baseline arrival spread over 30 days
        arrival_offset = timedelta(
            days=random.randint(0, 25),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59),
        )
        current_time = base_time + arrival_offset

        # 1. Triage
        records.append(
            {
                "case_id": patient_id,
                "activity": "ER Triage",
                "timestamp": current_time,
                "department": "Emergency",
                "resource": "Triage_Nurse",
                "severity": severity,
                "age": age,
                "cost": 150,
            }
        )

        # 2. Initial Assessment (15-60 mins later)
        current_time += timedelta(minutes=random.randint(15, 60))
        records.append(
            {
                "case_id": patient_id,
                "activity": "Initial Clinical Assessment",
                "timestamp": current_time,
                "department": "Emergency",
                "resource": "ER_Doctor",
                "severity": severity,
                "age": age,
                "cost": 300,
            }
        )

        # 3. Diagnostics Pathway
        current_time += timedelta(minutes=random.randint(30, 90))
        records.append(
            {
                "case_id": patient_id,
                "activity": "Blood Test & Lab Work",
                "timestamp": current_time,
                "department": "Pathology",
                "resource": "Lab_Technician",
                "severity": severity,
                "age": age,
                "cost": 220,
            }
        )

        if severity in ["Moderate", "High", "Critical"]:
            # Imaging bottleneck: takes longer for Imaging
            current_time += timedelta(minutes=random.randint(90, 240))
            records.append(
                {
                    "case_id": patient_id,
                    "activity": "Diagnostic Imaging (X-Ray/CT)",
                    "timestamp": current_time,
                    "department": "Radiology",
                    "resource": "Radiologist",
                    "severity": severity,
                    "age": age,
                    "cost": 650,
                }
            )

        # 4. Specialist Review
        current_time += timedelta(minutes=random.randint(45, 120))
        records.append(
            {
                "case_id": patient_id,
                "activity": "Specialist Consultation",
                "timestamp": current_time,
                "department": "Specialist_OPD",
                "resource": "Lead_Consultant",
                "severity": severity,
                "age": age,
                "cost": 500,
            }
        )

        # 5. Treatment Decision / Intervention
        if severity == "Critical":
            current_time += timedelta(minutes=random.randint(30, 90))
            records.append(
                {
                    "case_id": patient_id,
                    "activity": "Surgical Intervention",
                    "timestamp": current_time,
                    "department": "Surgical_Ward",
                    "resource": "Surgeon_Team",
                    "severity": severity,
                    "age": age,
                    "cost": 3500,
                }
            )
            current_time += timedelta(hours=random.randint(24, 72))
            records.append(
                {
                    "case_id": patient_id,
                    "activity": "Inpatient Bed Admission",
                    "timestamp": current_time,
                    "department": "ICU_Ward",
                    "resource": "ICU_Staff",
                    "severity": severity,
                    "age": age,
                    "cost": 1800,
                }
            )
        else:
            current_time += timedelta(minutes=random.randint(30, 60))
            records.append(
                {
                    "case_id": patient_id,
                    "activity": "Medication Administration",
                    "timestamp": current_time,
                    "department": "General_Ward",
                    "resource": "Ward_Nurse",
                    "severity": severity,
                    "age": age,
                    "cost": 180,
                }
            )

        # 6. Discharge Assessment
        current_time += timedelta(hours=random.randint(2, 24))
        records.append(
            {
                "case_id": patient_id,
                "activity": "Discharge Assessment",
                "timestamp": current_time,
                "department": "Administration",
                "resource": "Duty_Physician",
                "severity": severity,
                "age": age,
                "cost": 120,
            }
        )

        # 7. Final Discharge
        current_time += timedelta(minutes=random.randint(15, 45))
        records.append(
            {
                "case_id": patient_id,
                "activity": "Post-Care Discharge",
                "timestamp": current_time,
                "department": "Administration",
                "resource": "Discharge_Coordinator",
                "severity": severity,
                "age": age,
                "cost": 80,
            }
        )

    df = pd.DataFrame(records)
    output_path = os.path.join("data", "raw_clinical_events.csv")
    df.to_csv(output_path, index=False)
    print(f"Generated {len(df)} clinical event records across {num_patients} patients.")
    print(f"File saved successfully to: {output_path}")


if __name__ == "__main__":
    generate_clinical_event_log()