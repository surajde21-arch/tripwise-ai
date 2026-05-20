def get_travel_tips(destination):
    destination = destination.title()

    tips = {
        "Arizona": {
            "dos": [
                "Carry enough water, especially near canyons and desert areas.",
                "Start outdoor activities early to avoid peak heat.",
                "Book popular attractions like Antelope Canyon in advance."
            ],
            "donts": [
                "Do not hike without checking weather alerts.",
                "Do not ignore park entry fees or permit rules.",
                "Do not depend on weak mobile signal in remote areas."
            ]
        },
        "Florida": {
            "dos": [
                "Carry sunscreen and light clothing.",
                "Check theme park ticket prices before planning.",
                "Keep rain protection because weather can change quickly."
            ],
            "donts": [
                "Do not underestimate traffic near tourist areas.",
                "Do not leave valuables visible in parked cars.",
                "Do not skip checking hurricane/weather alerts."
            ]
        }
    }

    return tips.get(destination, {
        "dos": ["Plan routes in advance.", "Keep emergency cash.", "Check local rules before visiting attractions."],
        "donts": ["Do not overpack your schedule.", "Do not ignore weather alerts.", "Do not rely only on one navigation app."]
    })