def calculate_trip_budget(days, budget, transport):
    stay_cost = days * 120
    food_cost = days * 50

    if transport == "Own Vehicle":
        transport_cost = days * 40
    elif transport == "Rental Car":
        transport_cost = days * 85
    else:
        transport_cost = days * 25

    total_cost = stay_cost + food_cost + transport_cost
    remaining_budget = budget - total_cost

    return {
        "stay_cost": stay_cost,
        "food_cost": food_cost,
        "transport_cost": transport_cost,
        "total_cost": total_cost,
        "remaining_budget": remaining_budget,
        "is_within_budget": remaining_budget >= 0
    }