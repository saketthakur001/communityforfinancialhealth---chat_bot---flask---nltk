from flask import Flask, render_template, request, jsonify
from bot_response import get_options, lemmatize, compare
import random
import spacy
import math

app = Flask(__name__)
nlp = spacy.load("en_core_web_lg")

# Define the patterns, didn't_get, and other necessary functions here

@app.route('/')
def home():
    return render_template('chatbot.html')

@app.route('/get_response', methods=['POST'])
def get_bot_response():
    user_input = request.form['user_input']
    response = get_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
