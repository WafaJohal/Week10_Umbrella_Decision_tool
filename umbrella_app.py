import streamlit as st
import pandas as pd
from graphviz import Digraph

# --- Probabilities ---
P_rain = 0.3           # Probability it rains
P_sunny = 1 - P_rain   # Probability it is sunny

st.title(" ☂️  Umbrella Decision Tool")

st.markdown("""
Welcome! This tool lets you explore decision theory using the classic **umbrella example** seen in class. 

You're deciding whether or not to take an umbrella, based on a weather forecast. Adjust the forecast quality, change utility values, and see how they affect your decision. Use the decision network diagram and live-updating tables to help visualise how belief and utility come together in expected utility computation.

Start by selecting a forecast observation and adjusting how reliable the forecast is.

🔍 **Tip for getting started**: Leave the forecast as "No Forecast" to explore decisions based purely on prior probabilities and utility values — a great way to understand how beliefs and preferences shape choices before introducing additional information.
""")


# User selects whether forecast was good or bad
forecast = st.selectbox("Observed forecast:", ["No Forecast", "Good", "Bad"])

# --- Decision Network Visualization using Graphviz ---

st.markdown("### Decision Network")
dot = Digraph()
dot.node("W", "Weather", shape="ellipse")
if forecast!="No Forecast":
    dot.node("F", "Forecast", shape="ellipse")
dot.node("D", "Decision", shape="box")
dot.node("U", "Utility", shape="diamond")
dot.edges([("W", "U"), ("D", "U")])
if forecast != "No Forecast":
    dot.edge("W", "F")
st.graphviz_chart(dot)

st.markdown("---")
st.markdown("Adjust the utilities for each outcome (0-100):")

# --- User inputs ---
col1, col2 = st.columns(2)
with col1:
    u_rain_umbrella = st.slider('Rain & Umbrella', 0, 100, 70)
    u_rain_no_umbrella = st.slider('Rain & No Umbrella', 0, 100, 0)
    u_sunny_umbrella = st.slider('Sunny & Umbrella', 0, 100, 20)
    u_sunny_no_umbrella = st.slider('Sunny & No Umbrella', 0, 100, 100)

with col2: 
    st.markdown("### Utility Table")
    utility_table = pd.DataFrame({
        'Weather': ['Rain ', 'Rain', 'Sunny', 'Sunny '],
        'Decision': ['Umbrella', 'No Umbrella', 'Umbrella', 'No Umbrella'],
        'Utility': [u_rain_umbrella, u_rain_no_umbrella, u_sunny_umbrella, u_sunny_no_umbrella]
    })
    st.dataframe(utility_table, use_container_width=True)

st.markdown("---")


# Only show value of information blurb if forecast is used
if forecast != "No Forecast":
    st.markdown("## Exploring Value of Information")
    st.markdown("### Forecast Information")
    st.info("You're now exploring the **value of information**: how a forecast can update your belief about the weather, potentially changing the decision you make.")


    st.markdown("""
        Adjust how informative the weather forecast is. The sliders below let you tune the reliability of the forecast:<br>
        - **P(Good Forecast | Rain)**: How often the forecast is good when it actually rains.<br>
        - **P(Good Forecast | Sunny)**: How often the forecast is good when it's actually sunny.<br><br>
        """, unsafe_allow_html=True)


    st.markdown("Adjust how informative the weather forecast is:")

    # Forecast slider: probability of good forecast given rain/sunny
    P_good_given_rain = st.slider('P(Good Forecast | Rain)', 0.0, 1.0, 0.8)
    P_good_given_sunny = st.slider('P(Good Forecast | Sunny)', 0.0, 1.0, 0.2)


# Bayesian update based on forecast
if forecast == "Good":
    numerator = P_good_given_rain * P_rain
    denominator = (P_good_given_rain * P_rain) + (P_good_given_sunny * P_sunny)
    P_rain_updated = numerator / denominator
    P_sunny_updated = 1 - P_rain_updated
elif forecast == "Bad":
    P_bad_given_rain = 1 - P_good_given_rain
    P_bad_given_sunny = 1 - P_good_given_sunny
    numerator = P_bad_given_rain * P_rain
    denominator = (P_bad_given_rain * P_rain) + (P_bad_given_sunny * P_sunny)
    P_rain_updated = numerator / denominator
    P_sunny_updated = 1 - P_rain_updated
else:
    P_rain_updated = P_rain
    P_sunny_updated = P_sunny



if forecast != "No Forecast":
    # --- Display tables ---

    st.markdown("### Weather Probability Table")
    prob_table = pd.DataFrame({
        'Weather': ['Rain', 'Sunny'],
        'P(Weather)': [P_rain, P_sunny],
        'P(Weather|Forecast)': [P_rain_updated, P_sunny_updated]
    })

    prob_table = prob_table.round(2)
    st.dataframe(prob_table.set_index(prob_table.columns[0]))



# Calculate expected utilities
EU_umbrella = P_rain_updated * u_rain_umbrella + P_sunny_updated * u_sunny_umbrella
EU_no_umbrella = P_rain_updated * u_rain_no_umbrella + P_sunny_updated * u_sunny_no_umbrella

# Decision
recommendation = "Take the umbrella" if EU_umbrella > EU_no_umbrella else "Leave the umbrella"

# Display results
st.markdown("""
<hr style='height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet); border: none;'>
""", unsafe_allow_html=True)
st.markdown("## Results:")
st.markdown(f"- Updated Probability of Rain: **{P_rain_updated:.2f}**")
st.markdown(f"- Expected Utility (Take Umbrella): **{EU_umbrella:.2f}**")
st.markdown(f"- Expected Utility (Leave Umbrella): **{EU_no_umbrella:.2f}**")
st.markdown(f"## Recommended Decision: **{recommendation}**")


