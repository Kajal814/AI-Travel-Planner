import streamlit as st

from chains import (
    generate_itinerary,
    recommend_hotels,
    estimate_budget
)

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ AI Travel Planner")
st.write(
    "Plan your journey with personalized itineraries, handpicked hotel recommendations, and smart budget planning."
)

st.divider()

# ----------------------------
# User Inputs
# ----------------------------

destination = st.text_input("📍 Destination")

days = st.number_input(
    "📅 Number of Days",
    min_value=1,
    max_value=30,
    value=3
)

budget = st.number_input(
    "💰 Budget",
    min_value=1000,
    value=20000,
    step=1000
)

st.divider()

# ----------------------------
# Generate Button
# ----------------------------

if st.button("🚀 Generate Travel Plan"):

    if destination == "":
        st.warning("Please enter a destination.")
    else:

        with st.spinner("Generating itinerary..."):
            itinerary = generate_itinerary(destination, str(days))

        with st.spinner("Finding hotels..."):
            hotels = recommend_hotels(
                destination,
                str(budget),
                itinerary
            )

        with st.spinner("Estimating budget..."):
            budget_plan = estimate_budget(
                destination,
                str(days),
                str(budget),
                hotels
            )

        st.success("Travel Plan Generated Successfully!")

        st.divider()

        st.subheader("🗺️ Travel Itinerary")
        st.write(itinerary)

        st.divider()

        st.subheader("🏨 Recommended Hotels")
        st.write(hotels)

        st.divider()

        st.subheader("💵 Budget Estimation")
        st.write(budget_plan)