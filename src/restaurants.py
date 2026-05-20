from data.restaurants_data import RESTAURANTS_DATA


def get_restaurant_recommendations(destination, cuisine):

    destination = destination.title()

    destination_data = RESTAURANTS_DATA.get(destination)

    if not destination_data:
        return ["No restaurant data available"]

    cuisine_data = destination_data.get(cuisine)

    if not cuisine_data:
        return ["No matching cuisine found"]

    return cuisine_data