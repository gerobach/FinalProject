# 🩸 Biomedical Data Science Analysis of Haematological and Inflammatory Biomarkers

---

## 📌 Project Metadata

**Data Source:** NHANES 2021–2023

**Population:** US adults aged ≥18 years

**Sample Size:** ~6,300 participants (varies by analysis)

**Domain:** Biomedical Data Analytics & Data Science

**Primary Outcome:** Systemic Inflammation (CRP)

---

## 🔍 Project Summary

This project investigates the relationships between obesity, smoking, alcohol consumption, metabolic dysfunction and systemic inflammation using nationally representative NHANES data.

Statistical and machine learning techniques were used to identify inflammatory and metabolic biomarker patterns, discover participant phenotypes and develop predictive models for elevated CRP concentrations.

The project combines biomedical domain knowledge with modern data analytics approaches including correlation analysis, regression modelling, Principal Component Analysis (PCA), K-Means clustering and Logistic Regression.

---

## 📘 Project Structure

### 1️⃣ Data Acquisition & Integration

* NHANES module selection
* Dataset import and merging
* Adult cohort creation
* Variable selection

### 2️⃣ Data Cleaning & Feature Engineering

* Missing value assessment
* Outlier exploration
* Variable standardisation
* Smoking score creation
* Alcohol exposure scoring
* Biomarker classification groups

### 3️⃣ Exploratory Data Analysis (EDA)

* Distribution analysis
* Missingness assessment
* Biomarker visualisation
* Group comparisons
* Correlation exploration

### 4️⃣ Statistical Analysis

* Spearman correlation analysis
* Smoking vs haematological biomarkers
* Alcohol vs liver biomarkers
* HbA1c vs CRP
* Triglycerides vs CRP
* Multiple linear regression

### 5️⃣ Principal Component Analysis (PCA)

* Dimensionality reduction
* Identification of dominant biomarker patterns
* Variance explained analysis

### 6️⃣ K-Means Clustering

* Discovery of inflammatory and metabolic phenotypes
* Participant subgroup analysis
* Cluster interpretation

### 7️⃣ Predictive Modelling

* Logistic Regression
* Elevated CRP prediction
* Confusion matrix evaluation
* Model performance assessment

### 8️⃣ Feature Importance Analysis

* Predictor coefficient interpretation
* Identification of key inflammatory drivers
* Predictor ranking

### 9️⃣ Clinical Interpretation & Conclusions

* Integration of statistical and machine learning findings
* Biomedical interpretation of identified patterns

---

## 🛠️ Technology Stack

**Python · pandas · NumPy · matplotlib · seaborn · scipy · statsmodels · scikit-learn · Jupyter Notebook**

---

## ✨ Key Findings

### 🔥 Obesity & Inflammation

* BMI demonstrated the strongest association with CRP (ρ ≈ 0.51)
* CRP increased progressively across BMI categories
* Obesity emerged as the strongest inflammatory risk factor

### 🚬 Smoking & Haematology

* Daily smokers exhibited ~19% higher WBC counts
* Daily smokers exhibited ~22% higher neutrophil counts
* Smoking showed a clear inflammatory signature in routine blood tests

### 🍺 Alcohol & Liver Biomarkers

* Alcohol quantity showed a stronger relationship with GGT than drinking frequency
* Participants consuming ≥5 drinks per occasion exhibited substantially higher GGT levels

### 🍬 Metabolic Dysfunction & Inflammation

* Participants with diabetes demonstrated almost double the CRP concentrations of the normal HbA1c group
* Elevated triglycerides were associated with substantially higher CRP concentrations

### 📊 Principal Component Analysis

* PC1 explained 36.7% of total variance
* PC2 explained 19.4% of total variance
* Together, PC1 and PC2 explained 56.1% of total variance

### 🧬 K-Means Clustering

Three distinct participant phenotypes were identified:

| Cluster   | Interpretation         |
| --------- | ---------------------- |
| Cluster 0 | Lower-Risk Profile     |
| Cluster 1 | Inflammatory Phenotype |
| Cluster 2 | Metabolic Phenotype    |

### 🤖 Logistic Regression

* Model Accuracy: **75.8%**
* BMI emerged as the strongest predictor of elevated CRP
* WBC count and gender were additional important predictors

---

## 🏁 Conclusion

Across exploratory analysis, statistical modelling and machine learning approaches, obesity emerged as the strongest and most consistent factor associated with systemic inflammation.

Smoking was associated with elevated inflammatory blood counts, alcohol consumption was associated with increased liver stress markers, and metabolic dysfunction was strongly linked to elevated CRP concentrations.

Multiple analytical approaches converged on the same overall finding, highlighting the close relationship between obesity, metabolic health and inflammatory burden.
