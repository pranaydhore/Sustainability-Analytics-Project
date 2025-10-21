"""
Sustainability Analytics & Carbon Dashboard (Enhanced Multi-View Version)
Author: Pranay Dhore
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# ----------------------------------------
# PAGE CONFIG
# ----------------------------------------
st.set_page_config(page_title="🌿 Sustainability Analytics Dashboard",
                   layout="wide", initial_sidebar_state="expanded")

st.title("🌍 Sustainability Analytics & Carbon Dashboard")
st.caption("Placement-Ready Data Analytics Project • Technical + Non-Technical Visualization")

# ----------------------------------------
# SIDEBAR CONTROLS
# ----------------------------------------
with st.sidebar:
    st.header("⚙️ Controls")
    source = st.radio("📂 Select Data Source", ["Auto-load (UCI Energy)", "Upload CSV"])
    carbon_intensity = st.slider("🌱 Carbon Intensity (kg CO₂ per kWh)", 0.1, 1.0, 0.45, 0.05)
    z_thresh = st.slider("🚨 Anomaly Z-score Threshold", 1.5, 4.0, 2.5, 0.1)
    show_tech = st.checkbox("Show Technical Analytics", value=True)
    st.markdown("---")
    st.markdown("👤 **By:** Pranay Dhore\n📊 Data Analytics + ML\n📅 2025")

# ----------------------------------------
# DATA LOADING
# ----------------------------------------
@st.cache_data
def load_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00374/energydata_complete.csv"
    df = pd.read_csv(url)
    df["date"] = pd.to_datetime(df["date"])
    df.rename(columns={"Appliances": "Appliance_Power", "lights": "Lights"}, inplace=True)
    df["Energy_kWh"] = df["Appliance_Power"] / 60
    df["Carbon_Emission"] = df["Energy_kWh"] * carbon_intensity
    return df

if source == "Auto-load (UCI Energy)":
    df = load_data()
else:
    uploaded = st.file_uploader("Upload CSV file", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
    else:
        st.warning("Please upload a CSV file to continue.")
        st.stop()

# ----------------------------------------
# FEATURE ENGINEERING
# ----------------------------------------
df["hour"] = df["date"].dt.hour
df["weekday"] = df["date"].dt.day_name()
df["day"] = df["date"].dt.date

daily_df = df.groupby("day")[["Energy_kWh", "Carbon_Emission"]].sum()
hourly_df = df.groupby("hour")["Energy_kWh"].mean().reset_index()
weekday_df = df.groupby("weekday")["Energy_kWh"].mean().reindex(
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

daily_df["z_score"] = stats.zscore(daily_df["Energy_kWh"])
daily_df["is_anomaly"] = (np.abs(daily_df["z_score"]) > z_thresh).astype(int)

# ----------------------------------------
# KPIs
# ----------------------------------------
total_energy = daily_df["Energy_kWh"].sum()
total_co2 = daily_df["Carbon_Emission"].sum()
avg_daily = daily_df["Energy_kWh"].mean()
peak_day = daily_df["Energy_kWh"].idxmax()

k1, k2, k3, k4 = st.columns(4)
k1.metric("⚡ Total Energy", f"{total_energy:,.2f} kWh")
k2.metric("🌍 Total CO₂ Emissions", f"{total_co2:,.2f} kg")
k3.metric("📅 Avg Daily Usage", f"{avg_daily:.2f} kWh")
k4.metric("🔥 Peak Day", f"{peak_day}")

st.markdown("---")

# ----------------------------------------
# VISUALIZATION TABS
# ----------------------------------------
tabs = st.tabs([
    "📈 Daily Trend", "⏰ Hourly Pattern", "📅 Weekday Comparison",
    "📊 Distribution & Stats", "🔗 Relationships", "🚨 Anomalies", "📘 Summary"
])

# === TAB 1 — DAILY TREND ===
with tabs[0]:
    st.subheader("📈 Daily Energy Consumption & Rolling Average")
    daily_df["7d_avg"] = daily_df["Energy_kWh"].rolling(7).mean()
    fig1 = px.line(daily_df, y=["Energy_kWh", "7d_avg"], title="Daily Energy Trend",
                   labels={"value": "Energy (kWh)", "variable": "Metric"},
                   color_discrete_sequence=["#0077b6", "#ff8800"])
    st.plotly_chart(fig1, use_container_width=True)

# === TAB 2 — HOURLY PATTERN ===
with tabs[1]:
    st.subheader("⏰ Average Hourly Energy Usage")
    fig2 = px.bar(hourly_df, x="hour", y="Energy_kWh",
                  title="Average Hourly Consumption (kWh)",
                  color="Energy_kWh", color_continuous_scale="Viridis")
    fig2.update_layout(xaxis=dict(dtick=1))
    st.plotly_chart(fig2, use_container_width=True)

# === TAB 3 — WEEKDAY ===
with tabs[2]:
    st.subheader("📅 Average Energy Usage by Weekday")
    fig3 = px.bar(x=weekday_df.index, y=weekday_df.values,
                  title="Average Energy by Day of Week",
                  color=weekday_df.values, color_continuous_scale="plasma")
    fig3.update_layout(xaxis_title="Weekday", yaxis_title="kWh")
    st.plotly_chart(fig3, use_container_width=True)

# === TAB 4 — DISTRIBUTIONS & STATS ===
with tabs[3]:
    st.subheader("📊 Statistical Distributions")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Daily Energy Distribution")
        fig4 = px.histogram(daily_df, x="Energy_kWh", nbins=40, marginal="box",
                            title="Energy Consumption Distribution", color_discrete_sequence=["#0096c7"])
        st.plotly_chart(fig4, use_container_width=True)

    with c2:
        st.markdown("#### Carbon Emission Distribution")
        fig5 = px.histogram(daily_df, x="Carbon_Emission", nbins=40, color_discrete_sequence=["#6a994e"],
                            title="Carbon Emission per Day")
        st.plotly_chart(fig5, use_container_width=True)

    st.markdown("### 📄 Descriptive Statistics Table")
    stats_table = daily_df[["Energy_kWh", "Carbon_Emission"]].describe().T
    st.dataframe(stats_table.style.highlight_max(axis=1, color="lightgreen"))

# === TAB 5 — RELATIONSHIPS ===
with tabs[4]:
    st.subheader("🔗 Relationships between Variables")
    scatter_cols = st.multiselect("Select columns to compare:", options=["T1", "T2", "T3", "RH_1", "RH_2", "Appliance_Power", "Lights"], default=["T1", "Appliance_Power"])
    if len(scatter_cols) >= 2:
        fig6 = px.scatter_matrix(df, dimensions=scatter_cols, color="Appliance_Power",
                                 title="Variable Relationship Matrix", height=600)
        st.plotly_chart(fig6, use_container_width=True)
    else:
        st.info("Select at least two columns to view scatter matrix.")

    st.markdown("### 🔍 Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(df[["Appliance_Power", "Lights", "T1", "RH_1", "T2", "RH_2"]].corr(),
                annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    st.pyplot(fig)

# === TAB 6 — ANOMALIES ===
with tabs[5]:
    st.subheader("🚨 Detected Anomalies (Z-score Method)")
    anomalies = daily_df[daily_df["is_anomaly"] == 1]
    if anomalies.empty:
        st.success("✅ No anomalies found (Z < threshold).")
    else:
        st.warning(f"{len(anomalies)} anomaly days found.")
        st.dataframe(anomalies[["Energy_kWh", "z_score"]])
        csv = anomalies.to_csv().encode("utf-8")
        st.download_button("📥 Download Anomaly Report", csv, "anomalies.csv", "text/csv")

    # Top/Bottom 5 energy days
    st.markdown("### 📊 Top & Bottom 5 Energy Days")
    c1, c2 = st.columns(2)
    with c1:
        st.write("**Top 5 High-Energy Days**")
        st.dataframe(daily_df.sort_values("Energy_kWh", ascending=False).head(5))
    with c2:
        st.write("**Bottom 5 Low-Energy Days**")
        st.dataframe(daily_df.sort_values("Energy_kWh").head(5))

# === TAB 7 — SUMMARY ===
with tabs[6]:
    st.subheader("📘 Analytical Summary")
    peak_hour = hourly_df.loc[hourly_df["Energy_kWh"].idxmax(), "hour"]
    best_day = weekday_df.idxmax()
    st.markdown(f"""
    - 📊 **Average Daily Energy Use:** {avg_daily:.2f} kWh  
    - 🔥 **Peak Hour:** {int(peak_hour)}:00 hrs  
    - 🌞 **Highest Usage Day:** {best_day}  
    - 🌍 **Total CO₂ Emission:** {total_co2:.2f} kg  
    - ⚡ **Efficiency Suggestion:** Reduce load between 9–11 PM and adopt solar backup.  
    - 🧠 **Insight:** Energy correlates with indoor temperature and appliance use — higher during evenings and weekends.
    """)
    st.markdown("#### Technical Summary Statistics")
    st.dataframe(daily_df[["Energy_kWh", "Carbon_Emission", "z_score"]].describe().T)

st.markdown("---")
st.caption("🌱 Built with Streamlit • Visualization-rich Dashboard • Pranay Dhore © 2025")

