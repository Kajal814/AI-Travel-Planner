from llm import llm
from prompts import itinerary_prompt, hotel_prompt, budget_prompt


# -----------------------------
# Chain 1: Generate Itinerary
# -----------------------------
itinerary_chain = itinerary_prompt | llm

# -----------------------------
# Chain 2: Recommend Hotels
# -----------------------------
hotel_chain = hotel_prompt | llm

# -----------------------------
# Chain 3: Estimate Budget
# -----------------------------
budget_chain = budget_prompt | llm



# Function 1

def generate_itinerary(source, destination, days):

    response = itinerary_chain.invoke({
        "source": source,       
        "destination": destination,
        "days": days
    })

    return response.content


# -----------------------------
# Function 2
# -----------------------------
def recommend_hotels(destination, budget, itinerary):

    response = hotel_chain.invoke({
        "destination": destination,
        "budget": budget,
        "itinerary": itinerary
    })

    return response.content

# -----------------------------
# Function 3
# -----------------------------
def estimate_budget(source, destination, days, budget, hotel):

    response = budget_chain.invoke({
        "source": source,
        "destination": destination,
        "days": days,
        "budget": budget,
        "hotel": hotel
    })

    return response.content

print("Loaded chains.py")
print("recommend_hotels args:", recommend_hotels.__code__.co_argcount)
print("recommend_hotels arg count:", recommend_hotels.__code__.co_argcount)