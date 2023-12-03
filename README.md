<div align="center">
    <br>Flight Fare Prediction with Deployment
    <h1 align="center">
        <img src="https://media.istockphoto.com/id/1562804822/photo/airplane-in-the-sky-with-thunder-and-lightning.jpg?s=612x612&w=0&k=20&c=DInkeLxq90tP0wAe8_MFpv1auIS2wzs8MCyc4CGZb78=" width="360" />
    </h1>

<h3 align="center">
Data-Driven Travel: Predict Flight Fares and Plan Your Budget Effectively.
</h3>
<br>
<br>

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Installation](#installation)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [Bug / Feature Request](#bug---feature-request)
  * [Future scope of project](#future-scope)

---

## 📍 Overview

This project focuses on predicting flight fares to help travelers make informed decisions when booking flights. Flight fares can be highly variable due to factors like airline, time of booking, route, and more. This predictive model utilizes machine learning techniques to forecast flight prices, enabling users to plan their travel budgets more effectively.

---

## 📂 Dataset

The Flight Fare Prediction dataset from Kaggle is a comprehensive collection of flight-related data designed for predicting the fares of flights. This dataset is widely used by data scientists and machine learning enthusiasts to develop and fine-tune predictive models that accurately estimate the cost of air travel. Let's take a closer look at this dataset:

  ## 📜 Dataset Overview

Source: Kaggle (https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh)

Description: The dataset contains a diverse range of features associated with flights, including departure and arrival cities, airlines, departure and arrival times, duration, stops, and more. It's designed to simulate real-world flight data to help researchers and data practitioners build effective models for predicting flight fares.

Features: The dataset includes a variety of features, such as:

- Airline: The airline company operating the flight.
- Date of Journey: The date when the flight journey is scheduled.
- Source: The departure city.
- Destination: The arrival city.
- Route: The route taken by the flight.
- Duration: The duration of the flight in hours and minutes.
- Total Stops: The number of stops during the journey.
- Additional Information: Supplementary information about the flight.
- Target Variable: The primary target variable is the "Price" column, which represents the flight fare in Indian Rupees (INR).

---

## ⚙️ Features

- Data Collection: The project starts by gathering historical flight data, including details such as departure and arrival locations, airline, departure time, and more.
- Data Preprocessing: Raw data is preprocessed, including handling missing values, converting categorical variables, and normalizing numerical features.
- Feature Engineering: Relevant features are identified, and new features might be created to enhance the predictive power of the model.
- Model Selection: Different machine learning algorithms are explored, such as regression models, ensemble methods, and deep learning, to find the best-performing model for the task.
- Model Training: The selected model is trained on a portion of the dataset, and hyperparameters are tuned to optimize performance.
- Evaluation: The model's performance is evaluated using metrics like mean absolute error, root mean squared error, and others to quantify its accuracy.
- Prediction: Users can input flight details, and the trained model will predict the fare for the given flight.
- Web Interface: The prediction functionality is integrated into a user-friendly web interface where users can interact with the model.

---

## 🛠 Project Structure

- data: Contains the dataset used for training and testing the model.
- notebooks: Jupyter notebooks demonstrating data preprocessing, feature engineering, model training, and evaluation.
- src: Python scripts for data preprocessing, model training, and web interface development.
- web_app: Files for the web interface, including HTML, CSS, and JavaScript components.

---

## 🚀 Getting Started

- Clone the repository: git clone https://github.com/ayushmehraa/Flight-Fare-Prediction.git
- Navigate to the project directory: cd flight-fare-prediction
- Install the required packages: pip install -r requirements.txt
- Run the Jupyter notebooks to explore data preprocessing, model training, and evaluation.
- Set up the web app by following instructions in the web_app directory.

---

## 🤖 Web App

Flask and Streamlit are both popular frameworks for creating web applications in Python. They serve different purposes and have their own strengths. Here's a brief overview of how you could use Flask and Streamlit to create web apps for flight fare prediction:

## 🌲Flask Web App for Flight Fare Prediction

##
