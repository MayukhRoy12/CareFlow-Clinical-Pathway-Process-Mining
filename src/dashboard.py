import streamlit as st
import pandas as pd
import os

# Configure the Streamlit page layout
st.set_page_config(page_title="CareFlow Clinical Dashboard", layout="wide")

st.title("CareFlow: Clinical Pathway Process Mining")
st.markdown("Interactive dashboard for tracking patient pathways and clinical bottlenecks.")

# Load Data efficiently using Streamlit's caching
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/cleaned_clinical_events.csv")
        pathways = pd.read_csv("reports/common_pathways.csv")
        throughput = pd.read_csv("reports/patient_throughput.csv")
        return df, pathways, throughput
    except FileNotFoundError:
        st.error("Data files not found. Please run the preprocessing and analysis scripts first.")
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

df, pathways, throughput = load_data()

if not df.empty:
    # Sidebar Filters
    st.sidebar.header("Data Controls")
    department_filter = st.sidebar.multiselect(
        "Filter by Department", 
        options=df['department'].dropna().unique(),
        default=df['department'].dropna().unique()
    )
    
    # KPI Metrics Row
    st.subheader("Key Performance Indicators")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Patients (Cases)", df['case:concept:name'].nunique())
    col2.metric("Total Clinical Events", len(df))
    col3.metric("Avg Patient Throughput (Hours)", round(throughput['duration_hours'].mean(), 1))

    # Activity Visualizations
    st.divider()
    row1_col1, row1_col2 = st.columns(2)
    
    with row1_col1:
        st.subheader("Clinical Activity Volume")
        # Filter data based on selection
        filtered_df = df[df['department'].isin(department_filter)]
        
        # Format the data to remove the colon (:) from the index name for Streamlit
        activity_counts = filtered_df['concept:name'].value_counts().rename_axis('Activity').reset_index(name='Count')
        
        st.bar_chart(activity_counts, x='Activity', y='Count')

    with row1_col2:
        st.subheader("Most Frequent Patient Pathways")
        st.dataframe(
            pathways.head(10), 
            column_config={
                "Clinical_Pathway": "Sequence of Events",
                "Patient_Count": "Number of Patients"
            },
            hide_index=True,
            use_container_width=True
        )

    st.markdown("---")
    st.caption("CareFlow Process Mining Dashboard - Infotact Solutions Data Analytics Internship")