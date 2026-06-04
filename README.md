# 🩸 Biomedical Data Science Analysis of Haematological and Inflammatory Biomarkers in NHANES Adults

---

## 📌 Project Overview

This project explores relationships between haematological parameters, inflammatory biomarkers and metabolic dysfunction using data from the National Health and Nutrition Examination Survey (NHANES).

The aim is to investigate how obesity, smoking, alcohol consumption and metabolic health relate to changes in blood-based biomarkers associated with systemic inflammation and cardiometabolic risk in adults.

The project combines biomedical domain knowledge with data analytics, statistical analysis and data science techniques using Python.

---

# 🎯 Project Objectives

- Build a clean analytical dataset from multiple NHANES modules
- Explore missingness, distributions and outliers in biomedical data
- Investigate relationships between:
  - Obesity and systemic inflammation
  - Smoking and inflammatory blood markers
  - Alcohol consumption and liver biomarkers
  - Diabetes and metabolic dysfunction
- Create meaningful derived biomarkers and ratios
- Apply statistical analysis to investigate biomarker relationships
- Explore patterns and subgroup structures within haematological and inflammatory profiles
- Develop predictive and exploratory biomedical data science workflows
- Generate clinically interpretable visualisations and findings

---

# 🔬 Research Questions

This project aims to investigate several biomedical questions, including:

- Does obesity associate with elevated inflammatory markers such as CRP and NLR?
- Do smokers show elevated white blood cell and neutrophil counts?
- Is alcohol consumption associated with elevated liver biomarkers such as GGT?
- Is Mean Cell Volume (MCV) associated with alcohol consumption and liver biomarkers? 
- Are triglycerides and HbA1c associated with inflammatory biomarkers?
- Does waist-to-hip ratio associate more strongly with inflammation than BMI?
- Which haematological biomarkers show the strongest associations with systemic inflammation?
- Can biomarker patterns identify distinct inflammatory or metabolic phenotypes within the population?

---

# 🗂️ Data Source

Data used in this project originates from:

- **NHANES** (National Health and Nutrition Examination Survey)
- Conducted by the **CDC** (Centers for Disease Control and Prevention)
- NHANES August 2021-August 2023 Dataset

🔗 https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?Cycle=2021-2023

NHANES combines:
- Interviews
- Physical examinations
- Laboratory testing

to assess the health and nutritional status of the U.S. population.

---

# 📦 Included NHANES Modules

| Module | Description |
|---|---|
| DEMO_L | Demographics |
| BMX_L | Body measurements |
| CBC_L | Complete blood count |
| BIOPRO_L | Biochemistry profile |
| BPXO_L | Blood pressure readings |
| BPQ_L | Blood pressure/cholesterol questionnaire |
| DIQ_L | Diabetes questionnaire |
| SMQ_L | Smoking questionnaire |
| ALQ_L | Alcohol questionnaire |
| HSCRP_L | High sensitivity CRP |
| HDL_L | HDL cholesterol |
| TCHOL_L | Total cholesterol |
| TRIGLY_L | Triglycerides & LDL |
| GHB_L | HbA1c |
| VID_L | Vitamin D |
| FERTIN_L | Ferritin |
| FOLFMS_L | Folate |

---

# 🛠️ Technologies Used

- Python
- pandas
- NumPy
- matplotlib
- seaborn
- Jupyter Notebook

Potential additional libraries:
- scipy
- statsmodels
- scikit-learn

---

# ⚙️ Data Processing Workflow

## 1️⃣ Data Import
- Imported NHANES `.xpt` files using pandas
- Loaded datasets into Python using loops and dictionaries

## 2️⃣ Variable Selection
- Selected clinically relevant haematological, inflammatory and metabolic biomarkers
- Removed unnecessary or duplicate measurements
- Filtered dataset to adult participants only (`age >= 18`)

## 3️⃣ Data Structuring
- Grouped datasets into logical biomedical domains
- Merged datasets using participant ID (`SEQN`)

## 4️⃣ Feature Engineering

Created derived variables including:
- Mean systolic blood pressure
- Mean diastolic blood pressure
- Mean pulse
- Waist-to-hip ratio
- Neutrophil-to-lymphocyte ratio (NLR)
- Non-HDL cholesterol

## 5️⃣ Data Cleaning
- Removed invalid questionnaire codes
- Converted questionnaire variables to categorical datatypes
- Standardised column names
- Investigated missingness and outliers
- Explored skewed biomarker distributions

## 6️⃣ Exploratory Data Analysis (EDA)

Planned EDA includes:
- Distribution analysis
- Missingness visualisation
- Outlier assessment
- Correlation heatmaps
- Scatterplots
- Grouped biomarker comparisons
- Histograms and boxplots
- Haematological and inflammatory biomarker relationship exploration

---

# 📊 Planned Statistical Analysis

The project will include statistical investigation of biomarker relationships using approaches such as:

- Correlation analysis
- Group comparisons
- Association analysis
- Regression modelling
- Subgroup analysis
- Inflammatory marker association analysis

Potential analyses include:
- Smokers vs non-smokers inflammatory profiles
- Obesity vs CRP/NLR relationships
- Alcohol intake vs liver biomarker analysis
- HbA1c vs inflammatory biomarker relationships
- Predictors of elevated inflammatory markers

---

# 🤖 Planned Data Science Approaches

The project will also explore more advanced data science techniques to investigate hidden structure and predictive relationships within the dataset.

Planned approaches include:
- Identification of biomarker-based population subgroups
- Exploration of inflammatory and haematological phenotypes
- Pattern recognition within inflammatory and metabolic biomarkers
- Feature importance analysis
- Predictive modelling of inflammatory and metabolic outcomes
- Dimensionality reduction and high-dimensional data exploration
- Cluster and subgroup visualisation

Potential goals include:
- Identifying distinct inflammatory phenotypes
- Exploring haematological patterns associated with metabolic dysfunction
- Investigating relationships between obesity, inflammation and blood-based biomarkers
- Understanding which biomarkers contribute most strongly to inflammatory and cardiometabolic risk patterns

---

# 🧪 Key Variables of Interest

## 🩸 Haematological Biomarkers
- WBC
- Neutrophils
- Lymphocytes
- Monocytes
- NLR
- Haemoglobin
- Hematocrit
- MCV
- MCHC
- RDW
- Platelets

## 🔥 Inflammatory Biomarkers
- CRP
- Ferritin

## 🍬 Metabolic Biomarkers
- HbA1c
- Glucose
- Triglycerides
- HDL
- LDL
- Non-HDL cholesterol

## 🧫 Liver Biomarkers
- ALT
- AST
- GGT

## 📏 Anthropometric Variables
- BMI
- Waist circumference
- Waist-to-hip ratio

## 🚬 Lifestyle Variables
- Smoking status
- Alcohol consumption

---

# 🚧 Current Status

### ✅ Completed
- Dataset import
- Variable selection
- Dataset merging
- Adult cohort filtering
- Initial cleaning
- Questionnaire code cleaning
- Derived biomarker creation
- Missingness exploration
- Initial EDA

### 🔄 In Progress
- Distribution analysis
- Outlier assessment
- Correlation analysis
- Statistical testing

---

# 🔮 Future Work

Potential future extensions include:
- Advanced predictive modelling
- Biomarker clustering analysis
- Risk stratification approaches
- Additional subgroup analyses
- Expanded multivariable analysis
- Additional visual analytics
- Model comparison and evaluation

---

# ⚠️ Disclaimer

NHANES data is publicly available and fully anonymised.

This project is intended solely for educational and analytical purposes and does not constitute clinical research or medical advice.