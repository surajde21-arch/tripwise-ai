from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_ai_itinerary(
    destination,
    days,
    budget,
    transport,
    stay_type,
    cuisine
):

    prompt = f"""
    Create a detailed travel itinerary.

    Destination: {destination}
    Number of Days: {days}
    Budget: ${budget}
    Transportation: {transport}
    Stay Preference: {stay_type}
    Cuisine Preference: {cuisine}

    Include:
    - Morning activities
    - Afternoon activities
    - Evening activities
    - Restaurant suggestions
    - Budget-friendly recommendations
    - Famous attractions
    - Travel tips

    Keep it realistic and organized day-wise.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content