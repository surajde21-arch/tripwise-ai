def calculate_transport_cost(transport_type, days, miles_per_day=80, fuel_price=3.50, mpg=28):
    if transport_type == "Own Vehicle":
        gallons_needed = (miles_per_day * days) / mpg
        cost = gallons_needed * fuel_price

        return {
            "mode": "Own Vehicle",
            "estimated_cost": round(cost, 2),
            "details": f"Based on {miles_per_day} miles/day, {mpg} MPG, and ${fuel_price}/gallon."
        }

    elif transport_type == "Rental Car":
        rental_cost = days * 55
        fuel_cost = ((miles_per_day * days) / mpg) * fuel_price
        total = rental_cost + fuel_cost

        return {
            "mode": "Rental Car",
            "estimated_cost": round(total, 2),
            "details": f"Includes estimated rental cost plus fuel for {miles_per_day} miles/day."
        }

    else:
        cost = days * 25

        return {
            "mode": "Public Transport",
            "estimated_cost": round(cost, 2),
            "details": "Estimated daily public transport/pass cost."
        }