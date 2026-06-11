import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("football_match_predictor.pkl")

# Page Config
st.set_page_config(
    page_title="Football Match Outcome Prediction",
    page_icon="⚽",
    layout="wide"
)

# Title
st.title("⚽ International Football Match Outcome Predictor")

st.markdown("""
Predict whether the **Home Team** will win using:

- FIFA Rankings
- FIFA Points
- Elo Ratings
- Home Advantage
- Machine Learning (Random Forest)
""")

st.divider()

# Inputs
col1, col2 = st.columns(2)

with col1:

    st.subheader("🏠 Home Team")

    home_team = st.text_input(
        "Home Team",
        "Argentina"
    )

    home_rank = st.number_input(
        "Home FIFA Rank",
        min_value=1,
        max_value=250,
        value=1
    )

    home_points = st.number_input(
        "Home FIFA Points",
        value=1886.0
    )

    home_elo = st.number_input(
        "Home Elo Rating",
        value=2100.0
    )

with col2:

    st.subheader("✈️ Away Team")

    away_team = st.text_input(
        "Away Team",
        "Brazil"
    )

    away_rank = st.number_input(
        "Away FIFA Rank",
        min_value=1,
        max_value=250,
        value=5
    )

    away_points = st.number_input(
        "Away FIFA Points",
        value=1770.0
    )

    away_elo = st.number_input(
        "Away Elo Rating",
        value=2050.0
    )

st.divider()

home_advantage = st.radio(
    "Match Venue",
    ["Home Ground", "Neutral Venue"]
)

home_advantage = 1 if home_advantage == "Home Ground" else 0

# Feature Engineering
rank_difference = away_rank - home_rank

elo_difference = home_elo - away_elo

input_df = pd.DataFrame({

    "home_rank":[home_rank],

    "away_rank":[away_rank],

    "home_points":[home_points],

    "away_points":[away_points],

    "home_elo":[home_elo],

    "away_elo":[away_elo],

    "rank_difference":[rank_difference],

    "elo_difference":[elo_difference],

    "home_advantage":[home_advantage]

})

# Prediction
if st.button("Predict Match Outcome"):

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0]

    st.subheader("📊 Prediction Result")

    if prediction == 1:

        st.success(
            f"🏆 Predicted Winner: {home_team}"
        )

        st.metric(
            "Home Team Win Probability",
            f"{probability[1]*100:.2f}%"
        )

    else:

        st.error(
            f"🏆 Predicted Winner: {away_team}"
        )

        st.metric(
            "Away Team Win Probability",
            f"{probability[0]*100:.2f}%"
        )

    st.divider()

    st.subheader("Feature Values")

    st.dataframe(input_df)

# Footer
st.markdown("---")
st.markdown(
    "Built by **Prasanna Deshmane** | Machine Learning | FIFA Rankings | Elo Ratings | Streamlit"
)
