# Task-2
# 🫀 Heart Failure Prediction - Exploratory Data Analysis (EDA)

This repository contains an Exploratory Data Analysis (EDA) on the **Heart Failure Prediction Dataset**, available on [Kaggle](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction).  
The goal is to gain insights into the dataset through visualizations and statistical summaries to better understand the patterns related to heart disease.

---

## 📁 Dataset Description

**Features:**

- `Age` – Age of the patient
- `Sex` – Gender (Male/Female)
- `ChestPainType` – Type of chest pain experienced
- `RestingBP` – Resting blood pressure
- `Cholesterol` – Serum cholesterol in mg/dl
- `FastingBS` – Fasting blood sugar (>120 mg/dl)
- `RestingECG` – Resting electrocardiographic results
- `MaxHR` – Maximum heart rate achieved
- `ExerciseAngina` – Exercise-induced angina (Yes/No)
- `Oldpeak` – ST depression induced by exercise
- `ST_Slope` – Slope of the peak exercise ST segment
- `HeartDisease` – Target variable (1 = has heart disease, 0 = no heart disease)

---

## 🧪 Exploratory Data Analysis Steps

### ✅ Data Understanding
- Dataset shape and data types
- Summary statistics (mean, median, std, etc.)
- Missing value check

### 📊 Visualizations
- **Histogram** plots of all numeric features
- **Boxplots** for outlier detection
- **Countplots** for categorical variables like `Sex`, `ChestPainType`, `ExerciseAngina`
- **Correlation heatmap** to understand feature relationships
- **Pairplot** to study feature interactions

---

## 📈 Key Insights

- Age and `Oldpeak` values show a visible difference across heart disease groups.
- Males show higher heart disease prevalence than females in this dataset.
- Strong correlation observed between `MaxHR`, `Oldpeak`, and target variable.
- `ChestPainType` and `ST_Slope` appear to be significant categorical indicators.

---

## 🛠️ Tools & Libraries

- Python 3.x
- Pandas
- Matplotlib
- Seaborn
- Plotly (optional)

---


