# Dalele Application for Tourism: Recommender System Project Using Machine Learning

### Project Overview
The Dalele application is designed as a tourism recommendation system leveraging machine learning to suggest places of interest to users based on various factors, including textual reviews, geolocation, and categorical attributes. This recommender system integrates multiple data sources, including attraction details, user reviews, and geolocation information, to provide personalized recommendations for tourists exploring Cairo, Egypt.

Features
#### Multi-Source Data Integration:
Combines data from different sources, including attraction places, user reviews, and geographical locations.
#### Geohash-Based Recommendations: 
Utilizes geohash encoding to represent locations, allowing recommendations to consider spatial proximity.
#### Cosine Similarity for Recommendations:
Implements cosine similarity to find similarity in text-based features, providing recommendations based on user reviews and other textual data.
#### One-Hot Encoding for Categorical Data:
Encodes categorical data, such as attraction categories, for inclusion in the recommendation model.
#### TF-IDF Vectorization:
Uses Term Frequency-Inverse Document Frequency to vectorize textual data, extracting meaningful information from reviews.
Hybrid Approach to Recommendations: Combines multiple features, including text data, geolocation, categorical data, and numerical attributes like latitude, longitude, and ratings, to create a comprehensive recommendation system.
Model Persistence: 
Employs joblib to save the trained model, allowing for easy deployment and reusability.
Data Preparation
The project starts by reading and combining three data sources:

#### attractions.csv:
Contains details of various tourist attractions in Cairo.
reviews.csv: Includes reviews of these attractions, providing a rich source of textual data.
loc.csv: Contains geolocation information for each attraction.
These datasets are concatenated into a single dataframe for further processing.

Feature Engineering
Geohash Encoding: Adds a new column to the data, containing the geohash code for each attraction based on latitude and longitude.
One-Hot Encoding for Categorical Features: Transforms categorical attributes, such as "Category," into a format suitable for machine learning.
TF-IDF Vectorization for Text Data: Converts reviews into a TF-IDF matrix, extracting key information from textual content.
Cosine Similarity Calculation: Combines the TF-IDF matrix with numerical and categorical features to create a comprehensive feature set for calculating cosine similarity.
Recommendation System Logic
The recommendation system uses cosine similarity to determine the similarity between different attractions. It considers both textual reviews and spatial proximity (via geohash). The system then ranks the similarity scores and selects the top recommendations for a given place.
