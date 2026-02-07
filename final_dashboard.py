# =====================================================
# ST5011CEM – Big Data Programming Project
# FINAL DASHBOARD (Streamlit + ML)
# =====================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import os
import numpy as np

# ==================================
# Page Config
# ==================================
st.set_page_config(
    page_title="Public Transport Predictive Analytics",
    page_icon="🚌",
    layout="wide"
)

# ==================================
# LIGHT / CREAM THEME (EXAM SAFE)
# ==================================
st.markdown("""
<style>
.main {background-color:#fff7ed;color:#1f2937;}
h1,h2,h3 {color:#7c2d12;}
div[data-testid="metric-container"] {
    background:#ffedd5;
    border:1px solid #fed7aa;
    padding:18px;
    border-radius:14px;
}
section[data-testid="stSidebar"] {
    background:#fff7ed;
    border-right:1px solid #fed7aa;
}
button {
    background:#fb923c!important;
    color:white!important;
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

# ==================================
# Title
# ==================================
st.title("🚌 Public Transport Predictive Analytics Dashboard")
st.caption("GTFS-based Service Compliance • Location • Trends • Prediction")

# ==================================
# Load CSV Data
# ==================================
BASE_PATH = "/Users/manishakumarishah/Desktop/csv_files"

@st.cache_data
def load_csv(name):
    return pd.read_csv(f"{BASE_PATH}/{name}")

calendar = load_csv("calendar.csv")
calendar_dates = load_csv("calendar_dates.csv")
stops = load_csv("stops.csv")
frequencies = load_csv("frequencies.csv")

# ==================================
# Load ML Model
# ==================================
MODEL_PATH = f"{BASE_PATH}/trained_disruption_model.pkl"

@st.cache_resource
def load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None

model = load_model()

# ==================================
# Preprocessing
# ==================================
calendar_dates["service_removed"] = (
    calendar_dates["exception_type"] == 2
).astype(int)

calendar_dates["date"] = pd.to_datetime(
    calendar_dates["date"], format="%Y%m%d", errors="coerce"
)
calendar_dates["month"] = calendar_dates["date"].dt.month

# ==================================
# Sidebar Filters (FIXED – ALL 12 MONTHS)
# ==================================
st.sidebar.header("🔍 Filters")

month = st.sidebar.selectbox(
    "Select Month",
    list(range(1, 13))
)

filtered = calendar_dates[calendar_dates["month"] == month]

# ==================================
# KPI SECTION
# ==================================
st.markdown("## 📊 Key Performance Indicators")

k1, k2, k3, k4 = st.columns(4)

k1.metric("Total Services", calendar["service_id"].nunique())
k2.metric("Services Removed", int(filtered["service_removed"].sum()) if not filtered.empty else 0)
k3.metric("Total Stops", stops.shape[0])

avg_rate = filtered["service_removed"].mean() if not filtered.empty else 0
k4.metric("Avg Removal Rate", f"{avg_rate*100:.2f}%")

st.divider()

# ==================================
# DONUT CHART – REMOVAL %
# ==================================
st.subheader("🟠 Service Removal Ratio")

fig, ax = plt.subplots(figsize=(4, 4))

removed = filtered["service_removed"].sum() if not filtered.empty else 0
active = len(filtered) - removed if not filtered.empty else 0

ax.pie(
    [removed, active],
    labels=["Removed", "Active"],
    colors=["#fb923c", "#fde68a"],
    startangle=90,
    wedgeprops=dict(width=0.35)
)

ax.text(0, 0, f"{avg_rate*100:.1f}%", ha="center", va="center", fontsize=11)
st.pyplot(fig)

st.divider()

# ==================================
# LOCATION PLOT
# ==================================
st.subheader("📍 Transport Stop Locations")

fig, ax = plt.subplots(figsize=(8,5))
ax.scatter(stops["stop_lon"], stops["stop_lat"], alpha=0.4)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_title("Spatial Distribution of Stops")
st.pyplot(fig)

st.divider()

# ==================================
# PEAK HOURS
# ==================================
st.subheader("⏰ Peak Travel Hours")

frequencies["start_time"] = pd.to_datetime(
    frequencies["start_time"], errors="coerce"
)
frequencies["hour"] = frequencies["start_time"].dt.hour

hourly = frequencies.groupby("hour").size()

fig, ax = plt.subplots()
ax.bar(hourly.index, hourly.values, color="#fdba74")
ax.set_xlabel("Hour")
ax.set_ylabel("Trips")
st.pyplot(fig)

st.divider()

# ==================================
# MONTHLY TREND
# ==================================
st.subheader("📈 Monthly Service Removal Trend")

monthly = calendar_dates.groupby("month")["service_removed"].mean()
monthly = monthly.reindex(range(1,13), fill_value=0)

fig, ax = plt.subplots()
ax.plot(monthly.index, monthly.values, marker="o")
ax.set_xlabel("Month")
ax.set_ylabel("Removal Rate")
st.pyplot(fig)

st.divider()

# ==================================
# PREDICTION SECTION
# ==================================
st.subheader("🔮 Service Removal Risk Prediction")

if model is not None:
    sample = calendar.head(1).copy()

    feature_cols = [
        "monday","tuesday","wednesday",
        "thursday","friday","saturday","sunday",
        "start_month","end_month","service_duration"
    ]

    sample["start_month"] = 1
    sample["end_month"] = 12
    sample["service_duration"] = 30

    if st.button("Predict Service Removal Risk"):
        X = sample[feature_cols]
        pred = model.predict(X)[0]
        prob = model.predict_proba(X)[0][1]

        if pred == 1:
            st.error(f"⚠ High Risk of Service Removal (Probability: {prob:.2%})")
        else:
            st.success(f"✅ Low Risk (Confidence: {(1-prob):.2%})")
else:
    st.warning("⚠ Trained ML model not found.")

st.divider()

# ==================================
# DATA PREVIEW
# ==================================
st.subheader("📋 Filtered Data Preview")

st.dataframe(filtered.head(20), use_container_width=True)

st.download_button(
    "⬇ Download Filtered Data",
    filtered.to_csv(index=False),
    "service_removed_data.csv",
    "text/csv"
)

# ==================================
# Footer
# ==================================
st.caption(
    "Academic dashboard using public transport GTFS data "
    "(ST5011CEM – Big Data Programming)"
)

st.success("✅ FINAL DASHBOARD READY – Clean, Professional & Viva Safe")
