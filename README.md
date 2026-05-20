# TripWise AI

TripWise AI is an AI-powered travel planning application built using Python and Streamlit.

The application helps users plan trips based on:
- destination
- budget
- transportation mode
- stay preference
- cuisine preference
- travel duration

It generates:
- estimated trip costs
- budget summaries
- recommended attractions
- restaurant suggestions
- day-wise itineraries
- saved trip history

---

# 🚀 Features

## Current Features

- Budget-based trip planning
- Dynamic itinerary generation
- State-level destination recommendations
- Restaurant recommendation system
- Stay recommendation engine
- Expense visualization using Plotly
- SQLite database integration
- Saved trip history dashboard
- Modular backend architecture

---

# Tech Stack

## Frontend
- Streamlit

## Backend
- Python

## Database
- SQLite

## Data Processing
- Pandas

## Visualization
- Plotly

## AI Integration
- OpenAI API (in progress)

---

# 📂 Project Structure

```text
tripwise-ai/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── data/
│   ├── places_data.py
│   ├── restaurants_data.py
│   └── trips.db
│
├── src/
│   ├── ai_planner.py
│   ├── budget.py
│   ├── database.py
│   ├── itinerary.py
│   ├── restaurants.py
│   ├── stays.py
│   ├── transport.py
│   └── travel_tips.py