from langchain_core.prompts import PromptTemplate

# Chain 1: Travel Itinerary

itinerary_prompt = PromptTemplate(
   input_variables=["source", "destination", "days"],
    template="""

You are an expert travel planner.

The traveler is starting from {source}.

Destination: {destination}

Trip Duration: {days} days.

First, recommend the best mode of transportation from {source} to {destination}
(Flight, Train, Bus, or Car) with an approximate travel time.

Then create a detailed itinerary.

For each day include:
- Morning activity
- Afternoon activity
- Evening activity
- Recommended local food

Keep the itinerary realistic and well organized.
"""
)


# Chain 2: Hotel Recommendation

hotel_prompt = PromptTemplate(
    input_variables=["destination", "budget", "itinerary"],
    template="""
You are an expert travel advisor.

Based on the following itinerary:

{itinerary}

Recommend the 3 best hotels in {destination} that fit within a total trip budget of ₹{budget}.

For each hotel include:

- Hotel Name
- Approximate Price per Night
- Star Rating
- Key Amenities
- Nearby Attractions
- Reason for Recommendation

Recommend hotels that offer good value for money and are suitable for the planned itinerary.

Present the response in a clean, organized format.
"""
)

# -----------------------------
# Chain 3: Budget Estimation
# -----------------------------
budget_prompt = PromptTemplate(
    input_variables=["source", "destination", "days", "budget", "hotel"],
    template="""
You are an AI travel budget planner.

Destination: {destination}

Starting Location: {source}

Trip Duration: {days} days

Recommended Hotel:

{hotel}

User Budget: ₹{budget}

Estimate the following:

- Transportation Cost (from {source} to {destination})
- Hotel Cost
- Food Cost
- Local Transportation Cost
- Sightseeing Cost
- Miscellaneous Expenses
- Total Estimated Cost

Finally tell whether the trip is:

- Under Budget
- Within Budget
- Over Budget

Provide the response in a clean and well-structured format.
"""
)