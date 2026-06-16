import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt

from quality_checks import check_quality
from ai_insights import generate_insights, calculate_health_score

st.title("📊 AI Data Quality Copilot")

file = st.file_uploader("Upload CSV", type=["csv"])

st.write("Waiting for file upload...")

if file is not None:

    # LOAD DATA
    df = pd.read_csv(file)

    st.subheader("Dataset Preview")
    st.dataframe(df)

    # ANALYSIS
    report = check_quality(df)
    score = calculate_health_score(report)
    insights = generate_insights(report)

    # REPORT
    st.subheader("📌 Data Quality Report")
    st.json(report)

    # SCORE UI
    st.subheader("📊 Health Score")
    st.progress(score / 100)
    st.success(f"{score}/100")

    # CHART
    st.subheader("📉 Data Issues Chart")

    metrics = {
        "Missing": sum(report["Missing Values"].values()),
        "Duplicates": report["Duplicate Rows"],
        "Outliers": report["Outliers"],
        "Invalid Emails": report["Invalid Emails"]
    }

    fig, ax = plt.subplots()
    ax.bar(metrics.keys(), metrics.values())
    st.pyplot(fig)

    # AI INSIGHTS
    st.subheader("🤖 AI Insights")

    for i in insights:
        st.success(i)

    # DOWNLOAD REPORT
    st.download_button(
        "📥 Download Report",
        data=json.dumps(report, indent=4),
        file_name="data_quality_report.json",
        mime="application/json"
    )