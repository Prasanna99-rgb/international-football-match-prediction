import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("football_match_predictor.pkl")

st.set_page_config(
    page_title="⚽ Football Match Predictor",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ International Football Match Outcome Predictor")

st.markdown("""
Predict whether the **Home Team** will win using:

- FIFA Rankings
- FIFA Points
- Elo Ratings
- Home Advantage
""")

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("🏠 Home Team")

    home_team = st.text_input(
        "Home Team Name",
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
        value=1800.0
    )

    home_elo = st.number_input(
        "Home Elo Rating",
        value=2100.0
    )

with col2:

    st.subheader("✈️ Away Team")

    away_team = st.text_input(
        "Away Team Name",
        "Brazil"
    )

    away_rank = st.number_input(
        "Away FIFA Rank",
        min_value=1,
        max_value=250,
        value=3
    )

    away_points = st.number_input(
        "Away FIFA Points",
        value=1750.0
    )

    away_elo = st.number_input(
        "Away Elo Rating",
        value=2050.0
    )

st.divider()

home_advantage = st.selectbox(
    "Home Advantage",
    [1, 0],
    format_func=lambda x:
    "Yes" if x == 1 else "Neutral Venue"
)

rank_difference = away_rank - home_rank

elo_difference = home_elo - away_elo

input_data = pd.DataFrame({

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

if st.button("Predict Match"):

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0]

    st.subheader("📊 Prediction Result")

    if prediction == 1:

        st.success(
            f"🏆 {home_team} is predicted to WIN"
        )

        st.metric(
            "Winning Probability",
            f"{probability[1]*100:.2f}%"
        )

    else:

        st.error(
            f"🏆 {away_team} is predicted to WIN / Avoid Defeat"
        )

        st.metric(
            "Winning Probability",
            f"{probability[0]*100:.2f}%"
        )

    st.divider()

    st.subheader("Model Inputs")

    st.dataframe(input_data)
