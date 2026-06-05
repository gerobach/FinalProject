🩸 Biomedical Data Science Analysis of Inflammatory and Metabolic Biomarkers
📌 Project Metadata

Data Source: NHANES 2021–2023

Population: US adults aged ≥18 years

Sample Size: ~6,300 participants (varies by analysis)

Domain: Biomedical Data Analytics & Data Science

🔍 Project Summary

This project investigates relationships between obesity, smoking, alcohol consumption, metabolic dysfunction and systemic inflammation using nationally representative NHANES data.

Statistical and machine learning approaches were used to identify inflammatory and metabolic biomarker patterns, uncover population subgroups and develop predictive models for elevated CRP concentrations.

The project combines biomedical expertise with modern data analytics techniques including correlation analysis, regression modelling, Principal Component Analysis (PCA), K-Means clustering and Logistic Regression.

📘 Project Structure
1. Data Acquisition & Integration
NHANES module selection
Dataset merging
Adult cohort creation
2. Data Cleaning & Feature Engineering
Missing value assessment
Outlier exploration
Biomarker creation
Smoking and alcohol scoring
3. Exploratory Data Analysis
Distribution analysis
Biomarker visualisation
Group comparisons
4. Statistical Analysis
Correlation analysis
Smoking vs haematology
Alcohol vs liver biomarkers
HbA1c and triglycerides vs CRP
5. Principal Component Analysis (PCA)
Dimensionality reduction
Identification of dominant biomarker patterns
6. K-Means Clustering
Discovery of inflammatory and metabolic phenotypes
Participant subgroup analysis
7. Predictive Modelling
Logistic Regression
Elevated CRP prediction
Model evaluation
8. Feature Importance Analysis
Predictor coefficient interpretation
Identification of key inflammatory drivers
9. Conclusions & Clinical Interpretation

🛠️ Technology Stack

Python · pandas · NumPy · matplotlib · seaborn · scipy · statsmodels · scikit-learn · Jupyter Notebook

✨ Key Findings
Smoking was associated with elevated WBC and neutrophil counts.
Alcohol quantity showed a stronger relationship with GGT than drinking frequency.
Participants with diabetes and elevated triglycerides exhibited substantially higher CRP concentrations.
PCA identified distinct inflammatory and metabolic dimensions within the biomarker space.
K-Means clustering identified three participant phenotypes:
Lower-risk profile
Inflammatory phenotype
Metabolic phenotype
Logistic Regression achieved 75.8% accuracy in predicting elevated CRP.
BMI emerged as the strongest predictor of systemic inflammation across all analytical approaches.