from langchain_core.prompts import PromptTemplate

# -----------------------------
# Chain 1: Travel Itinerary
# -----------------------------
itinerary_prompt = PromptTemplate(
    input_variables=["destination", "days"],
    template="""
You are an expert travel planner.

Create a detailed {days}-day travel itinerary for {destination}.

For each day include:
- Morning activity
- Afternoon activity
- Evening activity
- Recommended local food

Keep the itinerary realistic and well organized.
"""
)

# -----------------------------
# Chain 2: Hotel Recommendation
# -----------------------------
hotel_prompt = PromptTemplate(
    input_variables=["destination", "budget", "itinerary"],
    template="""
You are a travel advisor.

Based on the following itinerary:

{itinerary}

Recommend 3 hotels in {destination} within a budget of {budget}.

For each hotel provide:
- Hotel Name
- Approximate Price per Night
- Key Features
- Reason for Recommendation
"""
)

# -----------------------------
# Chain 3: Budget Estimation
# -----------------------------
budget_prompt = PromptTemplate(
    input_variables=["destination", "days", "budget", "hotel"],
    template="""
You are a travel budget planner.

Destination: {destination}

Days: {days}

Recommended Hotel:

{hotel}

User Budget: {budget}

Estimate:

- Hotel Cost
- Food Cost
- Transportation Cost
- Sightseeing Cost
- Miscellaneous Expenses
- Total Estimated Cost

Finally tell whether the trip is:

- Under Budget
- Within Budget
- Over Budget
"""
)