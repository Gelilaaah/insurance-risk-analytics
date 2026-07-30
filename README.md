# 🛡️ Insurance Risk Analytics & Predictive Modeling

<p align="center">

### End-to-End Risk Analysis for South African Auto Insurance

**Turning historical insurance data into actionable insights for risk assessment, profitability, and data-driven pricing.**

</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas\&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikit-learn\&logoColor=white)
![DVC](https://img.shields.io/badge/DVC-Reproducibility-13ADC7?logo=dvc\&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC?logo=pytest\&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?logo=githubactions\&logoColor=white)

</p>

---

## 📌 Overview

**Insurance Risk Analytics & Predictive Modeling** is an end-to-end data science project developed using historical auto-insurance data from **AlphaCare Insurance Solutions (ACIS)**.

The project combines:

* 📊 Exploratory Data Analysis
* 📐 Statistical Hypothesis Testing
* 🤖 Predictive Modeling
* 🔍 Model Explainability
* 📈 Risk & Profitability Analysis
* 🔄 Reproducible Data Management
* 🧪 Automated Testing
* 📋 Business-Focused Reporting

The goal is to transform raw insurance data into **reliable, explainable, and actionable insights** that can support underwriting, risk assessment, customer segmentation, and pricing decisions.

---

# 🎯 Business Objective

AlphaCare Insurance Solutions is preparing to expand its presence in the **South African auto-insurance market**.

To compete effectively, ACIS needs to move beyond intuition-based decisions and understand how risk and profitability vary across its insurance portfolio.

This project investigates historical insurance data to answer questions such as:

> **Who is most likely to claim?**

> **Where is insurance risk highest?**

> **Which customer and vehicle segments are most profitable?**

> **Which factors drive claim severity?**

> **How can predictive analytics support better pricing and risk management?**

The ultimate objective is to provide ACIS with **evidence-based insights that can improve risk assessment, pricing strategies, and customer targeting.**

---

# 💼 Business Value

The analysis is designed to support several key insurance decisions:

| Business Area            | Potential Value                                          |
| ------------------------ | -------------------------------------------------------- |
| 🛡️ Risk Assessment      | Identify higher- and lower-risk customer segments        |
| 💰 Pricing               | Support data-driven premium strategies                   |
| 📊 Portfolio Management  | Monitor profitability and loss patterns                  |
| 👥 Customer Segmentation | Identify valuable customer groups                        |
| 🚗 Vehicle Risk          | Understand claim behavior across vehicle characteristics |
| 📍 Geographic Analysis   | Identify regional differences in insurance risk          |
| 🤖 Predictive Analytics  | Estimate claim probability and severity                  |
| 🔍 Explainable AI        | Understand the factors behind model predictions          |

---

# 📊 Dataset

The project uses approximately **18 months of historical South African auto-insurance data**, covering the period:

**February 2014 – August 2015**

The dataset contains information across several major categories:

| Category       | Description                                 |
| -------------- | ------------------------------------------- |
| 📄 Policy      | Policy identifiers and coverage information |
| 🔄 Transaction | Monthly transaction details                 |
| 👤 Client      | Demographic and account information         |
| 📍 Location    | Province and postal-code information        |
| 🚗 Vehicle     | Vehicle specifications and characteristics  |
| 📋 Plan        | Insurance plan and premium information      |
| 💰 Claims      | Premium and claims information              |

---

# 📐 Key Business Metrics

## Loss Ratio

The project uses **Loss Ratio** as a key measure of insurance portfolio performance.

[
\text{Loss Ratio} =
\frac{\text{Total Claims}}
{\text{Total Premium}}
]

A higher loss ratio generally indicates that a larger proportion of collected premiums is being consumed by claims.

```text
Lower Loss Ratio
       ↓
Lower Claims relative to Premium
       ↓
Potentially Better Portfolio Profitability
```

---

## Margin

Margin is calculated as:

[
\text{Margin} =
\text{Total Premium} -
\text{Total Claims}
]

It provides an indication of the contribution remaining after claims.

> **Note:** Margin is used as an analytical profitability indicator and does not represent complete accounting profit.

---

# 🔬 Analytical Approach

The project follows a structured end-to-end workflow:

```text
                 ┌─────────────────────┐
                 │   Raw Insurance Data │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Data Preparation    │
                 │ Cleaning & Validation│
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Exploratory Analysis│
                 │ Risk & Profitability│
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Hypothesis Testing  │
                 │ Statistical Evidence│
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Feature Engineering │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Predictive Modeling │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Model Evaluation    │
                 └──────────┬──────────┘
                            │
                 ┌──────────┴──────────┐
                 ▼                     ▼
          ┌──────────────┐      ┌──────────────┐
          │ SHAP / LIME  │      │ Business     │
          │ Explainability│      │ Insights     │
          └──────┬───────┘      └──────┬───────┘
                 │                     │
                 └──────────┬──────────┘
                            ▼
                 ┌─────────────────────┐
                 │ Stakeholder Report  │
                 └─────────────────────┘
```

---

# 🧪 Project Tasks

## Task 1 — Exploratory Data Analysis

The first stage focuses on understanding the insurance portfolio.

### Activities

* Data loading and validation
* Missing-value assessment
* Descriptive statistics
* Distribution analysis
* Outlier detection
* Geographic risk analysis
* Premium and claim analysis
* Loss Ratio calculation
* Margin analysis
* Visualization of key insurance metrics

### Key questions

* Which provinces have the highest loss ratios?
* How are claims distributed across the portfolio?
* How do premiums vary across customer groups?
* Are there significant outliers in claims or vehicle values?

---

# 📐 Task 2 — Hypothesis Testing

Statistical analysis is used to determine whether observed differences between groups are statistically significant.

### Areas investigated

* 👤 Gender groups
* 📍 Provinces
* 🚗 Vehicle characteristics
* 📮 Postal codes
* 💰 Premium groups
* 📊 Claim behavior

### Statistical methods

Depending on the characteristics of the data, the analysis uses methods such as:

* Two-proportion tests
* t-tests
* Mann–Whitney U tests
* ANOVA
* Kruskal–Wallis tests
* Chi-square tests where appropriate

The objective is to distinguish **statistically supported patterns from differences that may occur by chance.**

---

# 🤖 Task 3 — Predictive Modeling

The modeling stage applies machine learning to insurance risk prediction.

### Prediction objectives

#### Claim Probability

Estimate the likelihood that a policyholder will make a claim.

#### Claim Severity

Estimate the expected financial magnitude of claims.

#### Risk-Based Pricing

Explore how predictive analytics can support more informed premium and risk decisions.

### Models

Models evaluated include:

* Linear Regression
* Random Forest
* XGBoost

Models are compared using appropriate evaluation metrics and validation strategies.

---

# 🔍 Model Explainability

Predictive performance alone is not sufficient for high-stakes financial applications.

The project incorporates explainability techniques such as:

### SHAP

**SHAP (SHapley Additive exPlanations)** is used to understand:

* Which features have the greatest influence on predictions
* How individual features increase or decrease predicted risk
* Why a specific prediction was generated
* Whether unexpected or potentially concerning patterns exist

### LIME

Where applicable, **LIME** can provide local explanations for individual predictions.

The goal is to make model outputs more understandable to both technical and non-technical stakeholders.

---

# 🔄 Reproducibility

Reproducibility is a core engineering principle of the project.

The workflow uses **DVC (Data Version Control)** alongside Git to manage data-related artifacts and support reproducible experimentation.

The project also includes:

* Version-controlled source code
* Structured project directories
* Dependency management
* Reusable Python modules
* Automated testing
* Documented analytical workflows

---

# 🧪 Testing & Quality Assurance

Reliability is particularly important for financial and insurance analytics.

The project uses **pytest** to test critical components of the analytical pipeline.

Testing covers areas such as:

* Data loading
* Feature engineering
* Statistical functions
* Model-related functionality
* Utility functions

Automated checks are integrated into the development workflow through **GitHub Actions**.

---

# ⚙️ Technology Stack

### 🐍 Programming & Data Analysis

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Core programming language |
| Pandas     | Data manipulation         |
| NumPy      | Numerical computing       |
| SciPy      | Statistical analysis      |
| Matplotlib | Data visualization        |
| Seaborn    | Statistical visualization |

### 🤖 Machine Learning

| Technology        | Purpose                       |
| ----------------- | ----------------------------- |
| Scikit-learn      | Machine learning & evaluation |
| Random Forest     | Ensemble modeling             |
| XGBoost           | Gradient boosting             |
| Linear Regression | Regression baseline           |

### 🔍 Explainable AI

| Technology | Purpose                           |
| ---------- | --------------------------------- |
| SHAP       | Global & local model explanations |
| LIME       | Local model explanations          |

### 🛠️ Engineering & Reproducibility

| Technology     | Purpose                    |
| -------------- | -------------------------- |
| Git            | Version control            |
| GitHub         | Repository & collaboration |
| GitHub Actions | Continuous integration     |
| DVC            | Data version control       |
| Pytest         | Automated testing          |
| Jupyter        | Interactive analysis       |

---

# 📁 Project Structure

```text
insurance-risk-analytics/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_hypothesis_testing.ipynb
│   └── 03_modeling.ipynb
│
├── src/
│   ├── __init__.py
│   │
│   ├── data/
│   │   ├── __init__.py
│   │   ├── loader.py
│   │   └── preprocessing.py
│   │
│   ├── features/
│   │   ├── __init__.py
│   │   └── engineering.py
│   │
│   ├── statistics/
│   │   ├── __init__.py
│   │   └── hypothesis_tests.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── train.py
│   │   ├── predict.py
│   │   └── evaluate.py
│   │
│   ├── visualization/
│   │   ├── __init__.py
│   │   └── plots.py
│   │
│   ├── explainability/
│   │   ├── __init__.py
│   │   └── shap_utils.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
│
├── tests/
│   ├── test_data.py
│   ├── test_features.py
│   ├── test_statistics.py
│   └── test_models.py
│
├── reports/
│   └── final_report.md
│
├── models/
│
├── .dvc/
├── .gitignore
├── dvc.yaml
├── requirements.txt
└── README.md
```

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/Gelilaaah/insurance-risk-analytics.git
```

```bash
cd insurance-risk-analytics
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure DVC

If DVC has not already been initialized:

```bash
dvc init
```

> If the repository already contains a `.dvc` directory and DVC has already been initialized, do **not** run `dvc init` again.

---

## 5. Launch Jupyter

```bash
jupyter notebook
```

Then open:

```text
notebooks/01_eda.ipynb
```

---

# 📊 Key Business Questions

The project is designed to answer the following questions:

### Risk

* Which customer segments have the highest claim frequency?
* Which provinces demonstrate the highest insurance risk?
* Which vehicle characteristics are associated with higher claims?

### Profitability

* Which segments have the lowest and highest loss ratios?
* Which customer or vehicle groups contribute most to portfolio margin?
* Where are potential areas of poor portfolio performance?

### Claims

* Are there meaningful differences in claim behavior between customer groups?
* Are there geographic differences in claim frequency or severity?
* Are there temporal patterns in claims?

### Predictive Analytics

* Which variables best predict claim probability?
* Which variables best predict claim severity?
* Which model provides the strongest predictive performance?
* Why does the selected model make its predictions?

### Pricing

* How can predictive analytics support risk-based pricing?
* Which customer segments may require further pricing investigation?

---

# 📦 Deliverables

The completed project provides:

* ✅ Exploratory Data Analysis
* ✅ Statistical hypothesis testing
* ✅ Feature engineering pipeline
* ✅ Predictive risk models
* ✅ Model evaluation
* ✅ SHAP/LIME explainability
* ✅ Reproducible data workflow
* ✅ Automated testing
* ✅ CI/CD pipeline
* ✅ Business-focused visualizations
* ✅ Stakeholder-ready report
* ✅ Documented project structure

---

# ⚠️ Limitations

The results should be interpreted within the limitations of the available dataset.

Potential limitations include:

* Historical data may not fully represent current market conditions.
* The dataset covers a limited historical period.
* Observational data does not necessarily establish causality.
* Model predictions depend on the quality and representativeness of the training data.
* Demographic variables require careful consideration to avoid unintended discriminatory outcomes.
* Margin and loss ratio are analytical indicators and should not be interpreted as complete measures of accounting profitability.

---

# ⚖️ Ethical Considerations

Insurance analytics can directly influence financial outcomes for individuals and businesses. Responsible use of data is therefore essential.

This project emphasizes:

* 🔐 Responsible handling of insurance data
* 📋 Transparent documentation of assumptions
* 🔍 Explainable model predictions
* ⚖️ Careful consideration of demographic variables
* 🧪 Reproducible analytical processes
* 📊 Evidence-based decision-making
* 🚫 Avoidance of unsupported conclusions

Machine learning predictions should be treated as **decision-support information rather than automatic decisions**.

---

# 🔮 Future Improvements

Potential extensions include:

* Interactive Streamlit dashboard
* Real-time risk prediction API
* Automated model retraining
* Model monitoring and drift detection
* Automated data-quality monitoring
* Advanced hyperparameter optimization
* Model calibration
* Fairness and bias evaluation
* Cloud deployment
* Production model serving
* Integration with insurance management systems

---

# 📚 Documentation

Additional project documentation will include:

* 📓 EDA notebook
* 📐 Hypothesis testing notebook
* 🤖 Modeling notebook
* 📋 Technical report
* 📊 Dashboard
* 🔍 Model explainability analysis

---

# 👩🏽‍💻 Author

## Gelila Melaku

**Software Engineering Student | Data & AI Enthusiast**

| Task                              | Status       | Description                         |
| --------------------------------- | ------------ | ----------------------------------- |
| Task 1.2 – EDA & Statistics   | ✔️ Completed | Full EDA + insights + plots         |
| Task 2 – DVC & Pipeline Setup | ✔️ Completed | Reproducible data tracking          |
| Task 3 – Hypothesis Testing   | ✔️ Completed | Statistical analysis of risk        |
| Task 4 – Predictive Modeling  | ✔️ Completed | Claim prediction & feature 
