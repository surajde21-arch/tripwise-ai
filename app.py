import streamlit as st
import plotly.express as px
import pandas as pd
import sqlite3

from src.budget import calculate_trip_budget
from src.itinerary import generate_itinerary
from src.restaurants import get_restaurant_recommendations
from src.transport import calculate_transport_cost
from src.travel_tips import get_travel_tips
from src.database import create_trips_table, save_trip, get_all_trips
from src.ai_planner import generate_ai_itinerary

st.set_page_config(
    page_title="TripWise AI",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ TripWise AI")
st.subheader("AI-Powered Budget Travel Planner")

st.write("Plan smarter trips based on your budget, travel style, and schedule.")
create_trips_table()
# ---------------- USER INPUTS ---------------- #

destination = st.text_input("Enter destination state or city")

budget = st.number_input(
    "Enter your total budget ($)",
    min_value=0,
    value=500
)

transport = st.selectbox(
    "Transportation Type",
    [
        "Own Vehicle",
        "Rental Car",
        "Public Transport"
    ]
)

stay_type = st.selectbox(
    "Stay Preference",
    [
        "Airbnb",
        "Hotel",
        "Motel"
    ]
)

food_preference = st.selectbox(
    "Cuisine Preference",
    [
        "Indian",
        "Italian",
        "Mexican",
        "American",
        "Chinese"
    ]
)

travel_date = st.date_input("Travel Start Date")
return_date = st.date_input("Return Date")

days = (return_date - travel_date).days + 1

if days <= 0:
    st.error("Return date must be after or equal to the travel start date.")
else:
    st.info(f"🧳 Number of Travel Days: {days}")

# ---------------- GENERATE PLAN ---------------- #

if st.button("Generate Trip Plan") and days > 0:

    st.success("Trip Plan Generated Successfully!")

    st.markdown("## Suggested Itinerary")

    st.write(f"📍 Destination: {destination}")
    st.write(f"💰 Budget: ${budget}")
    st.write(f"📅 Travel Date: {travel_date}")
    st.write(f"🔁 Return Date: {return_date}")
    st.write(f"🧳 Total Days: {days}")
    st.write(f"🚗 Transport: {transport}")
    st.write(f"🏨 Stay Type: {stay_type}")
    st.write(f"🍴 Cuisine: {food_preference}")

    st.markdown("## Estimated Costs")

    budget_result = calculate_trip_budget(days, budget, transport)

    stay_cost = budget_result["stay_cost"]
    food_cost = budget_result["food_cost"]
    transport_cost = budget_result["transport_cost"]
    total_cost = budget_result["total_cost"]
    remaining = budget_result["remaining_budget"]
    save_trip(
        destination,
        budget,
        days,
        transport,
        stay_type,
        food_preference,
        total_cost,
        remaining
    )
    st.success("Trip saved to database.")

    st.markdown("## 💰 Estimated Costs")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="🏨 Stay Cost",
            value=f"${stay_cost}"
        )

    with col2:
        st.metric(
            label="🍴 Food Cost",
            value=f"${food_cost}"
        )

    with col3:
        st.metric(
            label="🚗 Transport Cost",
            value=f"${transport_cost}"
        )


    st.markdown("## 📊 Budget Summary")

    st.metric(
       label="💵 Remaining Budget",
       value=f"${remaining}"
    )
    st.markdown("## 📈 Expense Breakdown")

    expense_data = pd.DataFrame({
        "Category": ["Stay", "Food", "Transport"],
        "Cost": [stay_cost, food_cost, transport_cost]
    })

    fig = px.pie(
        expense_data,
        names="Category",
        values="Cost",
        title="Trip Expense Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    if remaining > 0:
        st.success("Trip fits within your budget!")
    else:
        st.error("Budget may not be enough for this trip.")
    
    st.markdown("## 🍽️ Recommended Restaurants")

    restaurants = get_restaurant_recommendations(
        destination,
        food_preference
    )

    for restaurant in restaurants:
        st.write(f"🍴 {restaurant}")

    st.markdown("## Day Wise Itinerary")

    ai_itinerary = generate_ai_itinerary(
        destination,
        days,
        budget,
        transport,
        stay_type,
        food_preference
    )

    st.markdown("## 🤖 AI Generated Itinerary")

    st.write(ai_itinerary)

    for plan in trip_plan:
         
         st.subheader(f"Day {plan['day']}")

         st.write(f"🌅 Morning: {plan['morning']}")
         st.write(f"🏞️ Afternoon: {plan['afternoon']}")
         st.write(f"🌇 Evening: {plan['evening']}")
    
    st.markdown("## ✅ Do’s and Don’ts")

    travel_tips = get_travel_tips(destination)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Do’s")
        for tip in travel_tips["dos"]:
            st.write(f"✅ {tip}")

    with col2:
        st.subheader("Don’ts")
        for tip in travel_tips["donts"]:
            st.write(f"❌ {tip}")
        
    st.markdown("## 🚗 Transport Cost Details")

    transport_result = calculate_transport_cost(transport, days)

    st.write(f"**Transport Mode:** {transport_result['mode']}")
    st.write(f"**Estimated Transport Cost:** ${transport_result['estimated_cost']}")
    st.write(f"**Details:** {transport_result['details']}")

    st.markdown("## 📁 Saved Trip History")

trips = get_all_trips()

if trips:
    trips_df = pd.DataFrame(
        trips,
        columns=[
            "Destination",
            "Budget",
            "Days",
            "Transport",
            "Stay Type",
            "Cuisine",
            "Total Cost",
            "Remaining Budget"
        ]
    )

    st.dataframe(trips_df, use_container_width=True)
else:
    st.info("No saved trips yet.")
