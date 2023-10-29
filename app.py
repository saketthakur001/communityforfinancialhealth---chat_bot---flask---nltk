from flask import Flask, render_template, request, jsonify
from chatbot import get_response, survey_time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chatbot.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    response = get_response(user_input)
    return jsonify({'response': response})

@app.route('/survey', methods=['POST'])
def survey():
    question_number = int(request.form['question_number'])
    user_input = request.form['user_input']
    selected_option, question_set, actual_question = survey_time(question_number, user_input)
    return jsonify({'selected_option': selected_option, 'question_set': question_set, 'actual_question': actual_question})

if __name__ == '__main__':
    app.run(debug=True)
