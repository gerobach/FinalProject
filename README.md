🩸 Biomedical Data Science Analysis of Inflammatory and Metabolic Biomarkers
📌 Project Overview

This project investigates the relationships between obesity, smoking, alcohol consumption, metabolic dysfunction and systemic inflammation using data from the National Health and Nutrition Examination Survey (NHANES).

By combining biomedical domain knowledge with statistical analysis and machine learning techniques, the project explores how lifestyle and metabolic factors influence inflammatory biomarkers and whether distinct participant phenotypes can be identified within the population.

📊 Project Metadata
Attribute	Details
Data Source	NHANES 2021–2023
Population	US adults aged ≥ 18 years
Sample Size	~6,300 participants (varies by analysis)
Domain	Biomedical Data Analytics & Data Science
Primary Outcome	Systemic inflammation (CRP)
🎯 Project Objectives

The project was designed to answer the following questions:

How strongly is obesity associated with systemic inflammation?
Do smokers exhibit elevated inflammatory blood markers?
Is alcohol consumption associated with liver biomarker changes?
How are metabolic biomarkers such as HbA1c and triglycerides related to inflammation?
Can distinct inflammatory and metabolic phenotypes be identified within the population?
Which factors best predict elevated CRP concentrations?
🗂️ Project Workflow
1. Data Acquisition & Integration
NHANES module selection
Dataset import and merging
Adult cohort creation
Variable selection
2. Data Cleaning & Feature Engineering
Missing value assessment
Outlier investigation
Variable standardisation
Smoking score creation
Alcohol exposure scoring
Biomarker group classification
3. Exploratory Data Analysis (EDA)
Distribution analysis
Missingness assessment
Biomarker visualisation
Group comparisons
Correlation exploration
4. Statistical Analysis
Spearman correlation analysis
Smoking vs haematological biomarkers
Alcohol vs liver biomarkers
HbA1c vs CRP
Triglycerides vs CRP
Multiple linear regression
5. Principal Component Analysis (PCA)
Dimensionality reduction
Identification of dominant biomarker patterns
Variance explained analysis
6. K-Means Clustering
Participant phenotype discovery
Cluster characterisation
Inflammatory vs metabolic subgroup analysis
7. Predictive Modelling
Logistic Regression
Elevated CRP prediction
Confusion matrix evaluation
Model performance assessment
8. Feature Importance Analysis
Logistic regression coefficient interpretation
Identification of key inflammatory drivers
Predictor ranking
9. Clinical Interpretation & Conclusions
Integration of statistical and machine learning findings
Biomedical interpretation of identified patterns
🛠️ Technology Stack
Programming & Analysis
Python
pandas
NumPy
Data Visualisation
matplotlib
seaborn
Statistical Analysis
scipy
statsmodels
Machine Learning
scikit-learn
PCA
K-Means Clustering
Logistic Regression
Development Environment
Jupyter Notebook
🔬 Key Biomarkers Investigated
Inflammatory Biomarkers
C-Reactive Protein (CRP)
Ferritin
Haematological Biomarkers
White Blood Cells (WBC)
Neutrophils
Lymphocytes
Monocytes
Haemoglobin
Haematocrit
Platelets
Neutrophil-to-Lymphocyte Ratio (NLR)
Metabolic Biomarkers
HbA1c
Triglycerides
HDL Cholesterol
LDL Cholesterol
Non-HDL Cholesterol
Liver Biomarkers
GGT
ALT
AST
Anthropometric Variables
BMI
Waist Circumference
Waist-to-Hip Ratio
✨ Key Findings
Smoking & Inflammation
Daily smokers exhibited approximately 19% higher WBC counts
Daily smokers exhibited approximately 22% higher neutrophil counts
Alcohol & Liver Function
Alcohol quantity showed a stronger relationship with GGT than drinking frequency
Participants consuming ≥5 drinks per occasion exhibited substantially higher GGT levels
Metabolic Health & Inflammation
Participants with diabetes demonstrated almost double the CRP concentrations observed in the normal HbA1c group
Elevated triglycerides were associated with substantially higher CRP concentrations
Principal Component Analysis
PC1 explained 36.7% of total variance
PC2 explained 19.4% of total variance
Together, the first two components explained 56.1% of total variance
K-Means Clustering

Three distinct participant phenotypes were identified:

Cluster	Interpretation
Cluster 0	Lower-Risk Profile
Cluster 1	Inflammatory Phenotype
Cluster 2	Metabolic Phenotype
Logistic Regression
Model accuracy: 75.8%
BMI emerged as the strongest predictor of elevated CRP
WBC count and gender were additional important predictors
🏁 Conclusion

Across exploratory analysis, statistical modelling and machine learning approaches, obesity emerged as the strongest and most consistent factor associated with systemic inflammation.

Smoking was associated with elevated inflammatory blood counts, alcohol consumption was associated with increased liver stress markers, and metabolic dysfunction was strongly linked to elevated CRP concentrations.

Multiple analytical approaches converged on the same overall finding, highlighting the close relationship between obesity, metabolic health and inflammatory burden.

⚠️ Limitations
NHANES is a cross-sectional dataset and does not allow causal inference
Several biomarkers contained missing values and were excluded from some analyses
Lifestyle variables were self-reported and may be subject to reporting bias
CRP was used as a surrogate marker of systemic inflammation
🚀 Future Work
Compare Logistic Regression with Random Forest and XGBoost models
Evaluate cluster validity using silhouette analysis
Investigate sex-specific and age-specific inflammatory profiles
Incorporate additional inflammatory biomarkers
Validate findings using external or longitudinal datasets
📄 Disclaimer

NHANES data are publicly available and fully anonymised.

This project was conducted for educational purposes as part of a Data Analytics and Data Science programme and does not constitute clinical research or medical advice.

This version looks much more like something you'd expect to see in a professional GitHub portfolio project. It also shows the full scope of what you actually did rather than underselling it.