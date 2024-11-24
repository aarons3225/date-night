from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

def load_movies():
    with open('movies.txt', 'r') as file:
        movies = []
        for line in file:
            parts = line.strip().split('|')
            movie = parts[0].strip()
            meal = parts[1].strip() if len(parts) > 1 else None
            movies.append((movie, meal))
        return movies

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spin')
def spin():
    movies = load_movies()
    selected_movie, associated_meal = random.choice(movies)
    return jsonify({
        "movie": selected_movie,
        "meal": associated_meal or "Random Food"  # Suggest random food if no meal is associated
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)