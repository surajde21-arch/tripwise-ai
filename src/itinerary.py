from data.places_data import PLACES_DATA


def generate_itinerary(destination, days):

    itinerary = []

    destination = destination.title()

    destination_data = PLACES_DATA.get(destination)

    if not destination_data:

        return [
            {
                "day": 1,
                "morning": f"Explore {destination}",
                "afternoon": "Visit popular attractions",
                "evening": "Try local restaurants"
            }
        ]

    places = destination_data["places"]
    sunrise = destination_data["sunrise"]
    sunset = destination_data["sunset"]

    for day in range(1, days + 1):

        place_index = (day - 1) % len(places)

        daily_plan = {
            "day": day,
            "morning": f"Visit {sunrise}",
            "afternoon": f"Explore {places[place_index]}",
            "evening": f"Watch sunset at {sunset}"
        }

        itinerary.append(daily_plan)

    return itinerary