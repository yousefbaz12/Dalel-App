from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the cosine similarity matrix
cosine_sim = joblib.load('cosine_similarity_model.pkl')

# Your dataset and other necessary data loading code
data = pd.read_csv('data.csv')


# Function to get place index from place name
def get_place_index(place_name, data):
    return data[data['Place Name'] == place_name].index[0]


# Function to get recommendations based on place name
def get_recommendations_by_name(place_name, cosine_sim=cosine_sim, data=data):
    place_index = get_place_index(place_name, data)
    sim_scores = list(enumerate(cosine_sim[place_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    recommended_indices = [i[0] for i in sim_scores[1:4]]  # Get top 3 recommendations
    return data['Place Name'].iloc[recommended_indices].tolist()


@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        content = request.json
        print(content)
        place_name = content['place_name']
        print(place_name)
        recommendations = get_recommendations_by_name(place_name)
        return jsonify({'recommendations': recommendations})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
