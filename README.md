# international-football-match-prediction
Machine Learning project that predicts international football match outcomes using FIFA Rankings, Elo Ratings, historical match data, Random Forest, XGBoost, and Streamlit.


# ⚽ International Football Match Outcome Prediction

## 📌 Project Overview

This project predicts the outcome of international football matches using Machine Learning techniques. The model leverages historical football match results, FIFA rankings, Elo ratings, and team performance indicators to estimate whether the home team is likely to win.

The objective is to demonstrate an end-to-end Machine Learning workflow, including data collection, preprocessing, feature engineering, model training, evaluation, and deployment using Streamlit.

---

## 🚀 Live Demo

### Try the Streamlit Application

🔗 https://international-football-match-prediction-vracwacyrkznbs3uvycjxc.streamlit.app/

---

## 🎯 Business Problem

Football analysts, fans, and sports organizations often seek data-driven methods to predict match outcomes.

This project aims to answer:

* Can historical football data predict future match outcomes?
* Which factors influence football match results the most?
* How do FIFA rankings and Elo ratings affect winning probability?

---

## 📂 Dataset Information

### Historical Match Results

* International football matches dataset
* Match results from international competitions

### FIFA Rankings

* FIFA World Rankings
* FIFA ranking points

### Elo Ratings

* Historical Elo ratings for international football teams

### Team Name Mapping

* Former team names and standardization mapping

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost
* Joblib
* Streamlit

---

## 🔍 Feature Engineering

The following features were created:

* Home FIFA Rank
* Away FIFA Rank
* Home FIFA Points
* Away FIFA Points
* Home Elo Rating
* Away Elo Rating
* Rank Difference
* Elo Difference
* Home Advantage

### Target Variable

```python
home_win = 1 if home_score > away_score else 0
```

---

## 🤖 Machine Learning Models

### Logistic Regression

Used as the baseline model.

### Random Forest

Used for handling nonlinear relationships and feature importance analysis.

### XGBoost

Used for advanced gradient boosting and performance optimization.

---

## 📊 Model Evaluation

Evaluation metrics used:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Cross Validation

---

## 📈 Key Insights

* Elo Rating Difference is one of the strongest predictors of match outcomes.
* FIFA Rank Difference significantly influences winning probability.
* Home Advantage improves the likelihood of winning.
* Combining FIFA Rankings and Elo Ratings produces stronger predictions than using either feature independently.

---

## 📁 Project Structure

```text
international-football-match-prediction/
│
├── app.py
├── football_match_predictor.pkl
├── requirements.txt
├── README.md
│
├── results.csv
├── fifa_ranking-2023-07-20.csv
├── eloratings.csv
├── former_names.csv
│
└── Football_Match_Prediction.ipynb
```

---

## ▶️ Run Locally

### Clone Repository

```bash
git clone https://github.com/Prasanna99-rgb/international-football-match-prediction.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Streamlit App

```bash
streamlit run app.py
```

---

## 📷 Streamlit Application Features

* Home Team Input
* Away Team Input
* FIFA Ranking Comparison
* Elo Rating Comparison
* Match Outcome Prediction
* Winning Probability Estimation

---

## 👨‍💻 Author

### Prasanna Deshmane

🔗 GitHub:
https://github.com/Prasanna99-rgb

🔗 LinkedIn:
https://www.linkedin.com/in/prasanna-deshmane-80a419205

---

## ⭐ Future Improvements

* Real-time FIFA Ranking API integration
* Team form and recent performance features
* Head-to-head statistics
* Advanced ensemble models
* Tournament simulation engine
* Interactive analytics dashboard

---

### If you found this project useful, please consider giving it a ⭐ on GitHub.

