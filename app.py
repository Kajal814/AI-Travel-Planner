import streamlit as st

from chains import (
    generate_itinerary,
    recommend_hotels,
    estimate_budget
)

st.set_page_config(
    page_title="AI Travel Planner",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>


.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1100px;
}


.stButton>button{
    width:100%;
    height:3rem;
    border-radius:8px;
    font-weight:600;
}


.stTextInput input,
.stNumberInput input{
    border-radius:8px;
}


.stSelectbox{
    border-radius:8px;
}


button[data-baseweb="tab"]{
    font-size:16px;
    font-weight:600;
}


div[data-testid="metric-container"]{
    border:1px solid #e6e6e6;
    border-radius:10px;
    padding:18px;
    background:white;
}

</style>
""", unsafe_allow_html=True)
st.title("AI Travel Planner")

st.caption(
    "Generate personalized travel itineraries, hotel recommendations, and budget estimation."
)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    source = st.text_input(
        "Source",
        placeholder="Enter your starting location"
    )

with col2:
    destination = st.text_input(
        "Destination",
        placeholder="Enter your destination"
    )

col3, col4 = st.columns(2)

with col3:
    days = st.number_input(
        "Duration (Days)",
        min_value=1,
        max_value=30,
        value=3
    )

with col4:
    budget = st.number_input(
        "Budget",
        min_value=1000,
        value=20000,
        step=1000
    )

travel_style = st.selectbox(
    "Travel Style",
    [
        "Budget",
        "Standard",
        "Luxury"
    ]
)

st.markdown("---")

generate = st.button(
    "Generate Travel Plan",
    use_container_width=True
)

if generate:

    if destination == "":
        st.warning("Please enter a destination.")
    else:

    with st.spinner("Generating your travel plan..."):

    itinerary = generate_itinerary(
        destination,
        str(days)
    )

    hotels = recommend_hotels(
        destination,
        str(budget),
        itinerary
    )

    budget_plan = estimate_budget(
        destination,
        str(days),
        str(budget),
        hotels
    )

      st.success("Travel plan generated successfully.")

st.markdown("---")

col1, col2, col3 = st.columns(3)

col1.metric("Duration", f"{days} Days")
col2.metric("Budget", f"₹{budget:,}")
col3.metric("Destination", destination)

st.markdown("---")

tab1, tab2, tab3 = st.tabs(
    [
        "Itinerary",
        "Hotels",
        "Budget"
    ]
)

with tab1:
    st.subheader("Travel Itinerary")
    st.markdown(itinerary)

with tab2:
    st.subheader("Recommended Hotels")
    st.markdown(hotels)

with tab3:
    st.subheader("Budget Estimation")
    st.markdown(budget_plan)
