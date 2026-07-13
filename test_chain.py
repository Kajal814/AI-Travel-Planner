from chains import (
    generate_itinerary,
    recommend_hotels,
    estimate_budget
)

destination = "Goa"
days = "3"
budget = "20000"

print("Generating Itinerary...\n")

itinerary = generate_itinerary(destination, days)
print(itinerary)

print("\nGenerating Hotels...\n")

hotels = recommend_hotels(destination, budget, itinerary)
print(hotels)

print("\nEstimating Budget...\n")

budget_plan = estimate_budget(destination, days, budget, hotels)
print(budget_plan)