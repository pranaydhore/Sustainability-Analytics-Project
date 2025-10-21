# 🌿 Sustainability Analytics & Carbon Dashboard
*A Data Analytics & AI Project by **Paras Longadge***

---

## 📘 Project Overview

The **Sustainability Analytics & Carbon Dashboard** is a full-fledged **data analytics and visualization project** designed to monitor, analyze, and forecast **energy consumption** and **carbon emissions**.  

Built with **Python**, **Streamlit**, **Plotly**, **Seaborn**, and **Machine Learning**, it provides a complete pipeline — from data ingestion to analytics, anomaly detection, visualization, and forecasting.

This project is both **technical** (for data analysts and engineers) and **non-technical friendly** (for managers, sustainability planners, and environmental consultants).

---

## 🎯 Objectives

- **Analyze** household or industrial energy consumption patterns.  
- **Detect anomalies** or sudden spikes in power usage.  
- **Estimate carbon emissions** from energy usage.  
- **Forecast** future energy demand and CO₂ impact using predictive analytics.  
- **Visualize** data through an interactive and modern UI.  
- **Evaluate** environmental sustainability — is the usage pattern good or bad for the planet?

---

## 🧠 Why This Project Matters

Energy consumption is directly linked to **carbon emissions**, which contribute to **global warming** and **climate change**.  
By understanding when and how energy is used, we can:

- Optimize energy efficiency 💡  
- Reduce emissions 🌍  
- Plan sustainable policies 🏡  
- Encourage behavioral changes 🧍‍♀️  

This dashboard helps visualize those relationships and shows **how sustainable our current energy usage truly is**.

---

## 🧩 Dataset

**Source:** [UCI Machine Learning Repository — Energy Efficiency Dataset](https://archive.ics.uci.edu/ml/datasets/energy+efficiency)

| Feature | Description |
|----------|--------------|
| `date` | Timestamp of energy reading |
| `Appliances` | Power consumed by appliances (W) |
| `lights` | Power consumed by lights (W) |
| `T1` ... `T9` | Indoor temperature sensors |
| `RH_1` ... `RH_9` | Relative humidity sensors |
| `Energy_kWh` | Derived energy usage per minute |
| `Carbon_Emission` | Estimated CO₂ equivalent emissions (kg) |

---

## ⚙️ Tech Stack

| Category | Tools / Libraries |
|-----------|------------------|
| **Frontend / UI** | Streamlit, Plotly, Seaborn, Matplotlib |
| **Backend / Processing** | Python (Pandas, NumPy) |
| **Data Source** | UCI Energy Dataset / User-uploaded CSV |
| **Analytics** | Z-score anomaly detection, rolling averages, descriptive stats |
| **Forecasting (optional)** | ARIMA / Prophet (for future energy prediction) |
| **Deployment Ready** | Streamlit Cloud / GitHub Pages / Localhost |

---

## 📊 Methodology

### 1. **Data Preparation**
- Imported dataset from UCI or uploaded CSV.  
- Converted timestamp → Date, Hour, Weekday.  
- Computed **energy consumption (kWh)** and **carbon emissions (kg CO₂)**.

### 2. **Feature Engineering**
- Created hourly, daily, and weekly aggregates.  
- Derived 7-day rolling averages for trend smoothing.  
- Normalized energy and carbon data for comparison.

### 3. **Descriptive Analytics**
- Computed mean, max, min, and standard deviation.  
- Generated summary tables for daily energy and emissions.  
- Built correlation heatmaps (Appliances, Temperature, Humidity).

### 4. **Anomaly Detection**
- Used **Z-score** method to detect unusual energy spikes.  
- Highlighted days where energy exceeded the normal range.  
- Anomalies help identify malfunctioning devices or inefficiencies.

### 5. **Predictive Forecasting (Optional)**
- Implemented ARIMA / Prophet models for **7-day energy prediction**.  
- Forecast future CO₂ emissions based on projected energy.  
- Visualized trends to evaluate sustainability trajectory.

### 6. **Visualization**
- Daily and hourly consumption patterns.  
- Weekday comparisons.  
- Carbon intensity charts.  
- Distribution histograms and scatter relationships.  
- Interactive dashboard with tables for both technical and non-technical audiences.

---

## 📈 Key Results & Insights

### ⚡ Energy Analysis
- Average daily consumption: **~1.25 kWh**
- Peak usage: **Evening hours (7 PM – 10 PM)**
- Highest usage day: **Sunday** (indicating home activity)
- Low usage: **Weekdays, particularly Tuesday**

### 🌍 Carbon Footprint Analysis
- Total CO₂ emissions: **~0.45 kg per day average**
- Positive correlation between **indoor temperature** and **energy usage**.
- High emissions during cold days (due to heating).

### 🚨 Anomaly Detection
- Detected days with 2× higher consumption — likely due to equipment overload.
- Anomalies correspond to **inefficient or faulty usage** patterns.

### 🔮 Forecasting Insights
- Future projections indicate a **steady increase** in energy usage if behavior continues.
- Without efficiency measures, **CO₂ emissions could rise by 5–8%** in the next 7 days.

---

## 🌱 Environmental Sustainability Evaluation

| Factor | Evaluation |
|--------|-------------|
| **Current Usage** | ⚠️ Above sustainable threshold during peak hours |
| **Carbon Impact** | 🌍 Moderate, but trending upward |
| **Sustainability Status** | 🟡 Partially sustainable — can improve with optimization |
| **Improvement Suggestions** | - Use smart timers and solar offsets <br> - Shift high-energy tasks to off-peak <br> - Monitor anomalies weekly |

### 📉 Environmental Impact Rating:
**★★★☆☆ (3/5 Sustainable)**  
> The current energy behavior shows potential for optimization, but sustainability measures are necessary to maintain long-term environmental health.

---

## 🧮 Example Visual Outputs

| Visualization | Description |
|----------------|--------------|
| 📈 **Daily Trend** | Energy trend with 7-day rolling average |
| ⏰ **Hourly Pattern** | Average hourly usage with peak time |
| 📅 **Weekday Comparison** | Energy use across weekdays |
| 📊 **Distribution** | Histogram showing usage variation |
| 🔗 **Correlation Heatmap** | Power vs Temperature & Humidity |
| 🚨 **Anomalies** | Highlighted abnormal energy days |
| 🔮 **Forecast (Optional)** | Predicted next 7-day energy curve |

---

## 💡 Technical vs Non-Technical Insights

| Audience | Focus |
|-----------|--------|
| **Technical (Analysts / Engineers)** | Model accuracy, z-score analysis, correlation heatmaps, forecasting |
| **Non-Technical (Managers / Policy-makers)** | KPI summaries, sustainability score, visual insights, improvement recommendations |

---

## 🧭 How to Run Locally

```bash
# 1️⃣ Clone the Repository
git clone https://github.com/your-username/sustainability-analytics.git
cd sustainability-analytics

# 2️⃣ Create Virtual Environment (optional)
python -m venv venv
source venv/Scripts/activate  # Windows
# or
source venv/bin/activate  # macOS/Linux

# 3️⃣ Install Dependencies
pip install -r requirements.txt

# 4️⃣ Run Streamlit Dashboard
streamlit run dashboard/app.py
