import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the trained model
model = pickle.load(open("xgb_model.pkl", "rb"))

# Function to predict flight price
def predict_flight_price(journey_date, dep_time, arrival_time, stops, airline, source, destination):
    # Extract features from input
    Journey_day = pd.to_datetime(journey_date).day
    Journey_month = pd.to_datetime(journey_date).month
    Dep_hour = dep_time.hour
    Dep_min = dep_time.minute
    Arrival_hour = arrival_time.hour
    Arrival_min = arrival_time.minute
    dur_hour = abs(Arrival_hour - Dep_hour)
    dur_min = abs(Arrival_min - Dep_min)

    # Map airline to one-hot encoded columns
    airlines = ["Jet Airways", "IndiGo", "Air India", "Multiple carriers", "Air Asia", "SpiceJet", "Vistara", "GoAir", "Multiple carriers Premium economy", "Jet Airways Business", "Vistara Premium economy", "Trujet"]
    airline_mapping = {a: 1 if a == airline else 0 for a in airlines}

    # Map source to one-hot encoded columns
    sources = ["Delhi", "Kolkata", "Banglore", "Mumbai", "Chennai"]
    source_mapping = {s: 1 if s == source else 0 for s in sources}

    # Map destination to one-hot encoded columns
    destinations = ["Cochin", "Banglore", "Delhi", "New Delhi", "Hyderabad", "Kolkata"]
    destination_mapping = {d: 1 if d == destination else 0 for d in destinations}

    features = [
        stops, Journey_day, Journey_month, Dep_hour, Dep_min, Arrival_hour, Arrival_min,
        dur_hour, dur_min, *airline_mapping.values(), *source_mapping.values(), *destination_mapping.values()
    ]

    # Make prediction
    prediction = model.predict(np.array([features]))

    return round(prediction[0], 2)

# Streamlit app
def main():
    # Page setup
    st.title("Flight Price Prediction")
    st.sidebar.header("User Input")

    # Enter Flight Details
    journey_date = st.sidebar.date_input("Date of Journey")
    dep_time = st.sidebar.time_input("Departure Time")
    arrival_time = st.sidebar.time_input("Arrival Time")
    stops = st.sidebar.selectbox("Number of Stops", [0, 1, 2, 3, 4])
    airline = st.sidebar.selectbox("Airline", ["Jet Airways", "IndiGo", "Air India", "Multiple carriers", "SpiceJet", "Vistara", "Air Asia", "GoAir", "Multiple carriers Premium economy", "Jet Airways Business", "Vistara Premium economy", "Trujet"])
    source = st.sidebar.selectbox("Source", ["Delhi", "Kolkata", "Banglore", "Mumbai", "Chennai"])
    destination = st.sidebar.selectbox("Destination", ["Cochin", "Banglore", "Delhi", "New Delhi", "Hyderabad", "Kolkata"])

    # Predict button
    if st.sidebar.button("Predict"):
        # Make prediction
        prediction = predict_flight_price(journey_date, dep_time, arrival_time, stops, airline, source, destination)

        # Convert to USD
        usd_prediction = round(prediction * 0.012)
        st.success(f"Your flight price prediction is Rs. {prediction} (Indian Rupees)")
        st.info(f"This is equivalent to ${usd_prediction} (United States Dollars)")
        st.success("Indian Rupee to US Dollar conversion — Last updated Dec 1, 2023, 04:41 UTC")

# Run the app
if __name__ == "__main__":
    main()
