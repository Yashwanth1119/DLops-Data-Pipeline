import streamlit as st
from main import run_pipeline
import pandas as pd
import os

st.title("📊 DLOps Data Pipeline with MongoDB")

if st.button("🚀 Run ETL Pipeline"):
    run_pipeline()
    st.success("Pipeline executed!")

    if os.path.exists("output/cleaned_data.csv"):
        df = pd.read_csv("output/cleaned_data.csv")
        st.subheader("✅ Cleaned Data")
        st.dataframe(df.head())
