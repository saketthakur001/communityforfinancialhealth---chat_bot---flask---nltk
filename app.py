from flask import Flask, render_template, request, jsonify
from chatbot import get_response, survey_time

app = Flask(__name)

@app.route('/')
def home():
    # Load the first survey question and options
    question_number = 2
    the_question, options, _ = survey_time(question_number, "")
    return render_template('chatbot.html', question=the_question, options=options)

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    response = get_response(user_input)
    return jsonify({'response': response})

@app.route('/survey', methods=['POST'])
def survey():
    question_number = int(request.json['question_number'])
    user_input = request.json['user_input']
    selected_option, question_set, actual_question = survey_time(question_number, user_input)

    # Load the next survey question and options
    next_question_number = question_number + 1
    next_the_question, next_options, _ = survey_time(next_question_number, "")

    return jsonify({
        'selected_option': selected_option,
        'question_set': question_set,
        'actual_question': actual_question,
        'next_question': next_the_question,
        'next_options': next_options,
        'next_question_number': next_question_number
    })

if __name__ == '__main__':
    app.run(debug=True)
